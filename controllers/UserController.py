import sys
from flask import json, request, make_response, jsonify
from sqlalchemy.sql.expression import table
from models.User import User

#Notification system model
from models.NotificationObject import NotificationObject
from models.NotificationChange import NotificationChange
from models.Notification import Notification
from models.EntityType import EntityType

#helpers
from helper.helper import *

from store.jwt_init import guard, flask_praetorian

from werkzeug.utils import secure_filename
import os
from store.app_store import app

#BASE_URL="https://api-zero-norn.herokuapp.com/"
BASE_URL="http://127.0.0.1:5000/"





@flask_praetorian.roles_required('admin')
def index():
    users=User().query.all()
    return jsonify([User.json(user) for user in users ])

def store():
    username=request.form.get('username',None)
    email=request.form.get('email',None)
    password=request.form.get('password',None)
    role=request.form.get('role',None)
    is_active=request.form.get('is_active',None)
    token_fcm=request.form.get('token_fcm',None)

    error_list=[]

    if(User.find_by_username(username)):
        error_list.append("username")
    if(User.find_by_email(email)):
        error_list.append("email")

    if(len(error_list)>0):
        return make_response(jsonify({"error_list":error_list}), 400)

    if(is_active=='0'):
        is_active=False
    else:
        is_active=True

    user = User.save(
        username=username,
        password=guard.hash_password(password),
        email=email,
        roles=role,
        is_active=is_active,
        token_fcm=token_fcm
        )

    if(user):
        #Here send the notification to admin
        user_admin=User.find_by_username("eliana")
        """
        print("this is the token of eliana")
        print(user_admin.token_fcm)
        send_notification_admin(user_admin.token_fcm, "Registro", "Se ha registrado un nuevo usuario a la base de datos... revisalo pls")
        """

        #Data Collection for action register
        # the 1 is for the user accions in table user
        entity_type=EntityType.get_by_id(1)
        entity_type_id=entity_type.id
        entity_id=user.id
        actor_id=user.id

        #List of notifiers
        notifiers=[user_admin.id]

        #Storing Notification Details
        storingNotificationDetails(
            entity_type_id=entity_type_id,
            entity_id=entity_id,
            actor_id=actor_id,
            notifiers=notifiers
        )

        #Generate a message for the list of notifiers 
        #And send this msg to every notifier in the list 

        msg=generate_notification_message(
            entity_type=entity_type,
            entity_id=entity_id
         )
        
        print("this is the msg of creacion of user ...")
        print(msg)
        for notifier in notifiers:
            send_notification_admin(user_admin.token_fcm,"registro de usuario",msg)

        return make_response(jsonify({"msg":"Usuario creado satisfactoriamente"}), 200)
    else:
        return make_response(jsonify({"error":"Se produjo un error al crear el usuario"}), 400)

def DataCollectionAndStoring():
    pass



def show(userId):
    user=User.get(userId)
    if(user):
        return make_response(jsonify({"user": User.json(user)},200))
    else:
        return make_response(jsonify({"msg":"Sucedio un error al mostrar el usuario"},400))

#Profile
def update(userId):
    username=request.form.get('username',None)
    email=request.form.get('email',None)
    password=request.form.get('password',None)
    role=request.form.get('role',None)

    user_old = User.get(userId)

    if(user_old.username!=username and User.find_by_username(username)):
        return make_response(jsonify({"error":"El nombre de usuario ya existe"}), 400)
    if(user_old.email!=email and User.find_by_email(email)):
        return make_response(jsonify({"error":"El correo electronico ya existe"}, 400))

    if(user_old.password!=password):
        new_password=guard.hash_password(password)
    else:
        new_password=password

    user = User.update(
        id=userId,
        username=username,
        password=new_password,
        email=email,
        roles=role,
        )
    if(user):
        return make_response(jsonify({"msg":"Usuario actualizado satisfactoriamente"}, 200))
    else:
        return make_response(jsonify({"error":"Se produjo un error al actualizar el usuario"}), 400)

def delete(userId):
    user=User.delete(userId)
    if(user):
        return make_response(jsonify({"msg":"Usuario eliminado correctamente"}, 200))
    else:
        return make_response(jsonify({"msg":"Sucedio un error al eliminar el usuario"}), 400)


#Paginado
@flask_praetorian.roles_required("admin")
def get_page():
    req=request.get_json(force=True)
    search=req.get('search', None)
    ini=req.get('ini', None)
    end=req.get('end', None)
 
    page=User.get_by_page(search=search, ini=ini, end=end)
    return make_response(jsonify([User.json(user) for user in page]),200)

#admin
@flask_praetorian.roles_required("admin")
def active_user(userId):
    user=User.activate_user(id=userId)
    print("in active endpoint")
    if(user.is_active and user.token_fcm!=None):
        #That works in base the admin user
        user_admin=User.find_by_username("eliana")

        #Data Collection for action register
        # the 1 is for the user accions in table user for activate account
        entity_type=EntityType.get_by_id(2)
        entity_type_id=entity_type.id
        entity_id=userId
        actor_id=user_admin.id

        #List of notifiers
        notifiers=[userId]

        #Storing Notification Details
        storingNotificationDetails(
            entity_type_id=entity_type_id,
            entity_id=entity_id,
            actor_id=actor_id,
            notifiers=notifiers
        )

        #Generate a message for the list of notifiers 
        #And send this msg to every notifier in the list 

        msg=generate_notification_message(
            entity_type=entity_type,
            entity_id=entity_id
         )
        
        send_notification_admin(user.token_fcm,"Cuenta activada",msg)

    elif (user.is_active==False and user.token_fcm!=None):
        #That works in base the admin user
        user_admin=User.find_by_username("eliana")

        #Data Collection for action register
        # the 1 is for the user accions in table user when admin inactiva an account 
        entity_type=EntityType.get_by_id(5)
        entity_type_id=entity_type.id
        entity_id=userId
        actor_id=user_admin.id

        #List of notifiers
        notifiers=[userId]

        #Storing Notification Details
        storingNotificationDetails(
            entity_type_id=entity_type_id,
            entity_id=entity_id,
            actor_id=actor_id,
            notifiers=notifiers
        )

        #Generate a message for the list of notifiers 
        #And send this msg to every notifier in the list 

        msg=generate_notification_message(
            entity_type=entity_type,
            entity_id=entity_id
        )
        print("that is user")
        print(user)
        
        send_notification_admin(user.token_fcm,"Cuenta Inactiva",msg)

    return make_response(jsonify(
        message="protected endpoint (allowed user {})".format(
            flask_praetorian.current_user().username,
        )
    ),200)

def login():
    req = request.get_json(force=True)
    username = req.get('username', None)
    password = req.get('password', None)
    token_fcm= req.get('token_fcm', None)

    user = guard.authenticate(username, password)

    ret={'access_token': guard.encode_jwt_token(user)}

    user_find=User.find_by_username(username=username)
    User.add_token_fcm(id=user_find.id, token_fcm=token_fcm)

    return make_response(jsonify(ret), 200)

def refresh():
    print("refresh request")
    old_token=request.get_data()
    new_token=guard.refresh_jwt_token(old_token)
    ret={'access_token':new_token}
    return make_response(jsonify(ret), 200)


@flask_praetorian.auth_required
def protected():
    return make_response(jsonify(
        message="protected endpoint (allowed user {})".format(
            flask_praetorian.current_user().username,
        )
    ),200)


def logout_msg():
    user_id=request.form.get('user_id',None)

    user_find=User.find_by_id(id=user_id)
    
    if(user_find):
        send_notification_admin(user_find.token_fcm,"We hope you come back soon","Sayonara")
        
    return make_response(jsonify({"msg":"Logout Successfully"}, 200))

