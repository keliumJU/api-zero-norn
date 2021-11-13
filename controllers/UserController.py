import sys
from flask import request, make_response, jsonify
from models.User import User
from store.jwt_init import guard, flask_praetorian

from werkzeug.utils import secure_filename
import os
from store.app_store import app

BASE_URL="http://127.0.0.1:5000/"

#Notification config
from pyfcm import FCMNotification
api_key="AAAAXIK7PVQ:APA91bGtkIJkCJ4rUYuA5MPBYXigeycsgwk69PQPQZLhym8XoQMgFmaoiXbfZ8FF4iJu7V9fI14C0455TcC6-eCOXtkJMb4lPQT3cIUcDVLdlYEk7MzNbsoUc-LtPpIttCVlsN4PkByX"

push_service = FCMNotification(api_key=api_key)

#Notifications test
def send_notification_admin(token, title, body):
    registration_id = token 
    message_title = title 
    message_body = body
    push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)



@flask_praetorian.roles_required('admin')
def index():
    users=User().query.all()
    return jsonify([User.json(user) for user in users ])

def store():
    username=request.form.get('username',None)
    email=request.form.get('email',None)
    password=request.form.get('password',None)
    name=request.form.get('name',None)
    role=request.form.get('role',None)
    is_active=request.form.get('is_active',None)
    token_fcm=request.form.get('token_fcm',None)
    file=request.files.get('img',None)

    if(User.find_by_username(username)):
        return {"error":"El nombre de usuario ya existe"}, 400
    if(User.find_by_email(email)):
        print(email)
        return {"error":"El correo electronico ya existe"}, 400

    if(file):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.root_path, "static/uploads/", filename))
        img_url=BASE_URL+'static/uploads/'+filename 
    else:
        img_url=None


    if(is_active=='0'):
        is_active=False
    else:
        is_active=True

    user = User.save(
        username=username,
        password=guard.hash_password(password),
        email=email,
        name=name,
        img=img_url,
        roles=role,
        is_active=is_active,
        token_fcm=token_fcm
        )

    if(user):
        #Here send the notification to admin
        user_admin=User.find_by_username("eliana")
        print("this is the token of eliana")
        print(user_admin.token_fcm)
        send_notification_admin(user_admin.token_fcm, "Registro", "Se ha registrado un nuevo usuario a la base de datos... revisalo pls")
        return {"msg":"Usuario creado satisfactoriamente"}, 200
    else:
        return {"error":"Se produjo un error al crear el usuario"}, 400


def show(userId):
    user=User.get(userId)
    if(user):
        return {"user": User.json(user)},200
    else:
        return {"msg":"Sucedio un error al mostrar el usuario"},400

#Profile
def update(userId):
    username=request.form.get('username',None)
    email=request.form.get('email',None)
    password=request.form.get('password',None)
    name=request.form.get('name',None)
    role=request.form.get('role',None)
    file=request.files.get('img',None)

    user_old = User.get(userId)

    if(user_old.username!=username and User.find_by_username(username)):
        return {"error":"El nombre de usuario ya existe"}, 400
    if(user_old.email!=email and User.find_by_email(email)):
        return {"error":"El correo electronico ya existe"}, 400

    if(file):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.root_path, "static/uploads/", filename))
        img_url=BASE_URL+'static/uploads/'+filename 
    else:
        img_url=user_old.img

    if(user_old.password!=password):
        print("new password: -->" + password)
        new_password=guard.hash_password(password)
    else:
        print("old password: -->" + password)
        new_password=password

    user = User.update(
        id=userId,
        username=username,
        password=new_password,
        email=email,
        name=name,
        img=img_url,
        roles=role,
        )
    if(user):
        return {"msg":"Usuario actualizado satisfactoriamente"}, 200
    else:
        return {"error":"Se produjo un error al actualizar el usuario"}, 400

def delete(userId):
    user=User.delete(userId)
    if(user):
        return {"msg":"Usuario eliminado correctamente"}, 200
    else:
        return {"msg":"Sucedio un error al eliminar el usuario"}, 400


#Paginado
@flask_praetorian.roles_required('admin')
def get_page():
    req=request.get_json(force=True)
    search=req.get('search', None)
    ini=req.get('ini', None)
    end=req.get('end', None)
 
    page=User.get_by_page(search=search, ini=ini, end=end)
    return jsonify([User.json(user) for user in page])

#admin
def active_user(userId):
    user=User.activate_user(id=userId)
    print("in active endpoint")
    if(user):
        print("user_active")
        print(user)
        print(user.token_fcm)
        if(user.is_active):
            send_notification_admin(user.token_fcm, "Cuenta activada", "Tu cuenta ha sido reconocida por el instituto. Ahora puedes iniciar sesion")
        else:
            send_notification_admin(user.token_fcm, "Cuenta Inactiva", "Tu cuenta ha sido desactivada por el instituto. Ahora no puedes iniciar sesion")
        return {"msg":"Usuario activado correctamente"},200
    else:
        return {"msg":"Sucedio un error al activar el usuario"}, 400

def login():
    req = request.get_json(force=True)
    username = req.get('username', None)
    password = req.get('password', None)
    token_fcm= req.get('token_fcm', None)

    user = guard.authenticate(username, password)

    ret={'access_token': guard.encode_jwt_token(user)}
    if(ret):
        user_find=User.find_by_username(username=username)
        add_token=User.add_token_fcm(id=user_find.id, token_fcm=token_fcm)
        if(add_token):
            return ret, 200

def refresh():
    print("refresh request")
    old_token=request.get_data()
    new_token=guard.refresh_jwt_token(old_token)
    ret={'access_token':new_token}
    return ret, 200


@flask_praetorian.auth_required
def protected():
    return {'message': f'protected endpoint (allowed user {flask_praetorian.current_user().username})'}




