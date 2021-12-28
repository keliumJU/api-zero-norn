from flask import json, request, make_response, jsonify
from sqlalchemy.sql.expression import desc

#Models involved 
from models.UserProfile import UserProfile 

#helpers
from helper.helper import *

from store.jwt_init import guard, flask_praetorian

from werkzeug.utils import secure_filename
import os
from store.app_store import app

#BASE_URL="https://api-zero-norn.herokuapp.com/"
BASE_URL="http://127.0.0.1:5000/"



LIMIT_PAGE=10

def index(user_id):
	user_profile=UserProfile.get(user_id)
	if(user_profile):
		return make_response(jsonify(UserProfile.json(user_profile)),200)
	else:
		return make_response(jsonify({"err":"El usuario todavia no ha creado un perfil"}),404)


def store():
	user_id=request.form.get('user_id',None)
	full_name=request.form.get('full_name',None)
	phone=request.form.get('phone',None)
	mobile=request.form.get('mobile',None)
	address=request.form.get('address',None)
	web_site=request.form.get('web_site',None)
	github=request.form.get('github',None)
	twitter=request.form.get('twitter',None)
	facebook=request.form.get('facebook',None)
	file=request.files.get('img',None)

	if(file):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.root_path, "static/uploads/", filename))
		img_url=BASE_URL+'static/uploads/'+filename 
	else:
		img_url=None

	user_profile = UserProfile.save(
		user_id=user_id,
		full_name=full_name,
		img=img_url,
		phone=phone,
		mobile=mobile,
		address=address,
		web_site=web_site,
		github=github,
		twitter=twitter,
		facebook=facebook
		)
	if(user_profile):
		return make_response(jsonify({"msg":"Perfil de usuario creado Satisfactoriamente"}), 200)
	else:
		return make_response(jsonify({"error":"Se produjo un error al crear el perfil del usuario"}), 400)

def update(user_id):
	full_name=request.form.get('full_name',None)
	phone=request.form.get('phone',None)
	mobile=request.form.get('mobile',None)
	address=request.form.get('address',None)
	web_site=request.form.get('web_site',None)
	github=request.form.get('github',None)
	twitter=request.form.get('twitter',None)
	facebook=request.form.get('facebook',None)
	file=request.files.get('img',None)
	img_no_update=request.form.get('img_no_update',None)
	print("this is img no update")
	print(img_no_update)

	print("data to update :)")
	print(full_name)
	print(phone)
	print(mobile)
	print(address)

	if(file):
		print("send a image")
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.root_path, "static/uploads/", filename))
		img_url=BASE_URL+'static/uploads/'+filename 
	else:
		if(img_no_update):
			img_url=img_no_update
		else:
			img_url=None

	user_profile = UserProfile.update(
		user_id=user_id,
		full_name=full_name,
		img=img_url,
		phone=phone,
		mobile=mobile,
		address=address,
		web_site=web_site,
		github=github,
		twitter=twitter,
		facebook=facebook
		)
	if(user_profile):
			return make_response(jsonify({"msg":"Perfil de usuario actualizado Satisfactoriamente"}), 200)
	else:
		return make_response(jsonify({"error":"Se produjo un error al actualizar el perfil del usuario"}), 400)

def delete(user_id):
    user_profile=UserProfile.delete(user_id)
    if(user_profile):
        return make_response(jsonify({"msg":"Perfil del usuario eliminado correctamente"}, 200))
    else:
        return make_response(jsonify({"msg":"Sucedio un error al eliminar el perfil del usuario"}), 400)
		