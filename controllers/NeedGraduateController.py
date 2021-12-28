from flask import json, request, make_response, jsonify
from models.NeedGraduate import NeedGraduate 

#helpers
from helper.helper import *

from store.jwt_init import guard, flask_praetorian


LIMIT_PAGE=10

def index():
	req=request.get_json(force=True)
	search=req.get('search', None)
	user_id=req.get('user_id',None)
	page_number = req.get('page_number', None)

	print("this is search")
	print(search)
	page=NeedGraduate.get_by_page(
		user_id=user_id,
		search=search, 
		ini=page_number*LIMIT_PAGE,
		end=LIMIT_PAGE
		)
	return make_response(jsonify([NeedGraduate.json(category) for category in page]),200)

def store():
	laboral_category_id=request.form.get('laboral_category_id',None)
	user_id=request.form.get('user_id',None)
	status=request.form.get('status',None)

	if(status=='1'):
		status=True
	elif (status=='0'):
		status=False

	need_graduate = NeedGraduate.save(
		laboral_category_id=laboral_category_id,
		user_id=user_id,
		status=status,
		)

	if(need_graduate):

		#Data Collection for action register
		# the 3 is for the user role <company> accions in table job_offer 
		entity_type=EntityType.get_by_id(4)
		entity_type_id=entity_type.id
		entity_id=need_graduate.id
		actor_id=need_graduate.user_id

		#List of notifiers

		notifiers=[]
		#here is the difficult ... because we have to search in need graduate table ... 
		job_offers =JobOffer.find_by_laboral_category_active(need_graduate.laboral_category_id)
		for offer in job_offers :
			notifiers.append(offer.user_id)

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

		list_tokens=User.get_tokens_by_list_ids(notifiers)
		send_multiple_devices(list_tokens, "Nueva necesidad de egresado", msg)

		"""
			AUTO SEND THIS USER ACTIVE NEED GRADUATE REGISTER	
			THAT IS INTERESTING
		"""
		entity_type=EntityType.get_by_id(3)
		entity_type_id=entity_type.id

		user_need_graduate=User.get(need_graduate.user_id)

		for job_offer in job_offers:
			#Data Collection for action register
			# the 3 is for the user role <company> accions in table job_offer 
			
			entity_id=job_offer.id
			actor_id=job_offer.user_id

			notifiers=[user_need_graduate.user_id]

			#Storing Notification Details
			storingNotificationDetails(
				entity_type_id=entity_type_id,
				entity_id=entity_id,
				actor_id=actor_id,
				notifiers=notifiers
			)
			#Generate a message for the list of notifiers 
			#And send this msg to every notifier in the list 

			#THE MESSAGE IS DIFF BECAUSE IS AN DIFFERENT USER
			msg=generate_notification_message(
				entity_type=entity_type,
				entity_id=entity_id
				)

			send_notification_admin(user_need_graduate.token_fcm, "Nueva oferta laboral", msg)


		return make_response(jsonify({"msg":"Necesidad egresado creada satisfactoriamente"}), 200)
	else:
		return make_response(jsonify({"error":"Se produjo un error al crear la Necesidad del egresado"}), 400)


def show(need_graduate_id):
    need_graduate=NeedGraduate.get(need_graduate_id)
    if(need_graduate):
        return make_response(jsonify({"need_graduate": NeedGraduate.json(need_graduate)},200))
    else:
        return make_response(jsonify({"msg":"Sucedio un error al mostrar la necesidad del egresado"},400))

def update(need_graduate_id):
	laboral_category_id=request.form.get('laboral_category_id',None)
	user_id=request.form.get('user_id',None)
	status=request.form.get('status',None)

	if(status=='1'):
		status=True
	elif (status=='0'):
		status=False

	need_graduate = NeedGraduate.update(
		id=need_graduate_id,	
		laboral_category_id=laboral_category_id,
		user_id=user_id,
		status=status,
		)
	if(need_graduate):
		return make_response(jsonify({"msg":"Necesidad del egresado actualizada satisfactoriamente"}, 200))
	else:
		return make_response(jsonify({"error":"Se produjo un error al actualizar la Necesidad del egresado"}), 400)

def delete(need_graduate_id):
    need_graduate=NeedGraduate.delete(need_graduate_id)
    if(need_graduate):
        return make_response(jsonify({"msg":"Necesidad del egresado eliminado correctamente"}, 200))
    else:
        return make_response(jsonify({"msg":"Sucedio un error al eliminar la Necesidad del egresado"}), 400)