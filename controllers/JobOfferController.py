from flask import json, request, make_response, jsonify
from sqlalchemy.sql.expression import desc

#Models involved 
from models.JobOffer import JobOffer 
from models.NeedGraduate import NeedGraduate 

#helpers
from helper.helper import *

from store.jwt_init import guard, flask_praetorian


LIMIT_PAGE=10

def index():
	req=request.get_json(force=True)
	search=req.get('search', None)
	user_id=req.get('user_id', None)
	page_number = req.get('page_number', None)

	page=JobOffer.get_by_page(
		user_id=user_id,
		search=search, 
		ini=page_number*LIMIT_PAGE,
		end=LIMIT_PAGE
		)
	return make_response(jsonify([JobOffer.json(need) for need in page]),200)

def store():
	laboral_category_id=request.form.get('laboral_category_id',None)
	user_id=request.form.get('user_id',None)
	type_offer=request.form.get('type_offer',None)
	salary=request.form.get('salary',None)
	description=request.form.get('description',None)
	status=request.form.get('status',None)

	if(status=='1'):
		status=True
	elif (status=='0'):
		status=False

	job_offer = JobOffer.save(
		laboral_category_id=laboral_category_id,
		user_id=user_id,
		type_offer=type_offer,
		salary=salary,
		description=description,
		status=status,
		)

	if(job_offer):
		
		#Data Collection for action register
		# the 3 is for the user role <company> accions in table job_offer 
		entity_type=EntityType.get_by_id(3)
		entity_type_id=entity_type.id
		entity_id=job_offer.id
		actor_id=job_offer.user_id

		#List of notifiers

		notifiers=[]
		#here is the difficult ... because we have to search in need graduate table ... 
		need_graduates=NeedGraduate.find_by_laboral_category_active(job_offer.laboral_category_id)
		for graduate in need_graduates:
			notifiers.append(graduate.user_id)

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
		print(msg)
		list_tokens=User.get_tokens_by_list_ids(notifiers)
		send_multiple_devices(list_tokens, "Nueva oferta laboral", msg)

		"""
			AUTO SEND THIS USER ACTIVE NEED GRADUATE REGISTER	
			THAT IS INTERESTING
		"""
		entity_type=EntityType.get_by_id(4)
		entity_type_id=entity_type.id

		user_job_offer=User.get(job_offer.user_id)

		for graduate in need_graduates:
			#Data Collection for action register
			# the 3 is for the user role <company> accions in table job_offer 
			
			entity_id=graduate.id
			actor_id=graduate.user_id

			notifiers=[job_offer.user_id]

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

			send_notification_admin(user_job_offer.token_fcm, "Nueva necesidad de egresado", msg)


		return make_response(jsonify({"msg":"Oferta laboral creada satisfactoriamente"}), 200)
	else:
		return make_response(jsonify({"error":"Se produjo un error al crear la oferta laboral"}), 400)


def show(job_offer_id):
    job_offer=JobOffer.get(job_offer_id)
    if(job_offer):
        return make_response(jsonify({"job_offer": JobOffer.json(job_offer)},200))
    else:
        return make_response(jsonify({"msg":"Sucedio un error al mostrar la oferta laboral"},400))

def update(job_offer_id):
	laboral_category_id=request.form.get('laboral_category_id',None)
	user_id=request.form.get('user_id',None)
	type_offer=request.form.get('type_offer',None)
	salary=request.form.get('salary',None)
	description=request.form.get('description',None)
	status=request.form.get('status',None)

	if(status=='1'):
		status=True
	elif (status=='0'):
		status=False

	job_offer = JobOffer.update(
		id=job_offer_id,
		laboral_category_id=laboral_category_id,
		user_id=user_id,
		type_offer=type_offer,
		salary=salary,
		description=description,
		status=status,
		)

	if(job_offer):
		return make_response(jsonify({"msg":"Oferta laboral actualizada satisfactoriamente"}, 200))
	else:
		return make_response(jsonify({"error":"Se produjo un error al actualizar la Oferta Laboral"}), 400)

def delete(job_offer_id):
    job_offer=JobOffer.delete(job_offer_id)
    if(job_offer):
        return make_response(jsonify({"msg":"Oferta Laboral eliminada correctamente"}, 200))
    else:
        return make_response(jsonify({"msg":"Sucedio un error al eliminar la Oferta Laboral"}), 400)
		