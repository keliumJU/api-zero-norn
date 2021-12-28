from flask import json, request, make_response, jsonify
#helpers
from helper.helper import *
from models.NotificationChange import NotificationChange 

from store.jwt_init import guard, flask_praetorian

from store.app_store import app

LIMIT_PAGE=10


def get_notifications_by_user_page():
	userId= request.args.get('userId',None)
	pageNumber = request.args.get('pageNumber',None)

	#Here resived the object
	req=request.get_json(force=True)
	filter_dict=req.get('filter_dict', None)

	if(pageNumber):
		pageNumber=int(pageNumber)
	
	print("this is the limit page")
	print(pageNumber*LIMIT_PAGE)
	notifications_user = notification_details_page(
		user_id=userId,
		filter_dict=filter_dict,
		page_ini=pageNumber*LIMIT_PAGE,
		page_end=LIMIT_PAGE
		)

	return make_response(jsonify([NotificationDetails.json(noti) for noti in notifications_user]),200)


def delete_notification():
    notifier_id=request.form.get('notifier_id',None)
    notification_object_id=request.form.get('notification_object_id',None)

    notification=Notification.delete_notifcation(notifier_id, notification_object_id)

    if(notification):
        return make_response(jsonify({"msg":"Notificación eliminada correctamente"}, 200))
    else:
        return make_response(jsonify({"msg":"Sucedio un error al eliminar la Notificación"}), 400)


def revised_notification():
	notifier_id=request.form.get('notifier_id',None)
	notification_object_id=request.form.get('notification_object_id',None)

	notification=Notification.change_status(notifier_id, notification_object_id)

	if(notification):
		return make_response(jsonify({"msg":"Notificación revisada correctamente"}, 200))
	else:
		return make_response(jsonify({"msg":"Sucedio un error al revisar la Notificación"}), 400)