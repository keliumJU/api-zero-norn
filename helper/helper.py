from flask_sqlalchemy import model

from models.JobOffer import JobOffer
from models.NeedGraduate import NeedGraduate 
from models.LaboralCategory import LaboralCategory 

from store.db_init import db
from models.Notification import Notification

from models.User import User 
from models.UserProfile import UserProfile 

from models.NotificationObject import NotificationObject
from models.NotificationDetails import NotificationDetails
from models.NotificationChange import NotificationChange 

from models.EntityType import EntityType


from sqlalchemy import desc


#Notification config
from pyfcm import FCMNotification
api_key="AAAAXIK7PVQ:APA91bGtkIJkCJ4rUYuA5MPBYXigeycsgwk69PQPQZLhym8XoQMgFmaoiXbfZ8FF4iJu7V9fI14C0455TcC6-eCOXtkJMb4lPQT3cIUcDVLdlYEk7MzNbsoUc-LtPpIttCVlsN4PkByX"

push_service = FCMNotification(api_key=api_key)

def storingNotificationDetails(entity_type_id, entity_id, actor_id, notifiers):
    #insert in notification object table
    notification_object=NotificationObject.save_data(
        entity_type_id=entity_type_id,
        entity_id=entity_id,
        status=False
        )
    #Get notification_object id
    notification_object_id=notification_object.id

    #insert in notification_change_table
    NotificationChange.save_data(
        notification_object_id=notification_object_id,
        actor_id=actor_id,
        status=False
        )

    #insert in notification table
    for notifier_id in notifiers:
        Notification.save_data(
            notification_object_id=notification_object_id,
            notifier_id=notifier_id,
            status=False
        )


def generate_notification_message(entity_type, entity_id):
    #Dynamic parts of message
    #username, action type(entity_type_id), user description(the value of the action)
    #{{username}} {{action type}} user, {{user description}}
    msg=""
    if(entity_type.id==1 or entity_type.id==2 or entity_type.id==5):
        
        #same table not problem but table is user
        user=User.find_by_id(entity_id)
        if(user):
            print("--->THIS IS JOB OFFER IN MSG<----")
            username=user.username
            action_type=entity_type.description
            table_description=user.email
        else:
            return 0
        msg='{0} {1} user {2}'.format(username,action_type,table_description)

    elif entity_type.id==3 : 
        #find in table job_offer
        #same table not problem but table is user
        job_offer=JobOffer.get(entity_id)
        if(job_offer):
            print("--->THIS IS JOB OFFER IN MSG<----")
            print(entity_id)
            print(job_offer)
            user=User.find_by_id(job_offer.user_id) 
            username=user.username
            action_type=entity_type.description
            table_description=job_offer.description
        else:
            return 0

        msg='{0} {1} need_graduate {2}'.format(username,action_type,table_description)

    elif entity_type.id==4 : 
        #find in table job_offer
        #same table not problem but table is user
        need_graduate=NeedGraduate.get(entity_id)
        if(need_graduate):
            print("--->THIS IS NEED GRADUATE IN MSG<----")
            print(entity_id)
            print(need_graduate)
            user=User.find_by_id(need_graduate.user_id) 
            username=user.username
            action_type=entity_type.description
            category=LaboralCategory.get(need_graduate.laboral_category_id)
            table_description=category.name
        else:
            return 0

        msg='{0} {1} need_graduate {2}'.format(username,action_type,table_description)

    else:
        pass

    return msg

def conditionFilter(obj, filter_dict):
    condition = db.and_(*[getattr(obj, col).ilike(f'{val}%') for col, val in filter_dict.items()])
    return condition


def notification_details_page(user_id, filter_dict=None,page_ini=0, page_end=10):
        #result = db.session.query(NotificationObject).join(Notification, NotificationObject.id==Notification.notification_object_id).filter_by(notifier_id = user_id).offset(page_ini).limit(page_end).all()
        #En lo posible hacelo con un join
        result=None
        if(filter_dict):
            if('status' not in filter_dict):
                result = db.session.query(NotificationObject,Notification)\
                .filter(NotificationObject.id==Notification.notification_object_id)\
                .filter(Notification.notifier_id==user_id, conditionFilter(NotificationObject, filter_dict)).order_by(desc(NotificationObject.created_on))\
                .offset(page_ini).limit(page_end).all()
            else:
                status=int(filter_dict['status'])
                del filter_dict['status']
                result = db.session.query(NotificationObject,Notification)\
                .filter(NotificationObject.id==Notification.notification_object_id)\
                .filter(Notification.notifier_id==user_id, conditionFilter(NotificationObject, filter_dict), Notification.status==status).order_by(desc(NotificationObject.created_on))\
                .offset(page_ini).limit(page_end).all()
        else:
            result = db.session.query(NotificationObject,Notification)\
                .filter(NotificationObject.id==Notification.notification_object_id)\
                .filter(Notification.notifier_id==user_id).order_by(desc(NotificationObject.created_on))\
                .offset(page_ini).limit(page_end).all()



        print("this is result")
        print(result)

        list_deatils_notification=[]
        for row in result:
            print("this is row")
            print(row[0])

            #Generate the message in base the entity_type
            #get the entity_type

            entityType=EntityType.get_by_id(row[0].entity_type_id)

            message=generate_notification_message(entityType, row[0].entity_id)

            if (message!=0):
                #Get user img
                notificationChange=NotificationChange.get_by_object_id(row[0].id)

                user_profile=UserProfile.get(notificationChange.actor_id)
                img_actor=None
                if(user_profile):
                    img_actor=user_profile.img
                #Save details
                detail=NotificationDetails(
                        object_id=row[0].id,
                        entity_id=row[0].entity_id, 
                        entity_type_id=row[0].entity_type_id,
                        notifier_id=user_id,
                        created_on=row[0].created_on,
                        message=message,
                        img_user=img_actor,
                        status=row[1].status
                    )
                list_deatils_notification.append(detail)
        return list_deatils_notification




def get_list_notifiers(notification_object_id):
	#list of notifiers
	notifiers=Notification.get_notifiers(notification_object_id)
	return notifiers 

#Notifications test
def send_notification_admin(token, title, body):
    registration_id = token 
    message_title = title 
    message_body = body
    push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body, click_action="http://localhost:3000/")

def send_multiple_devices(tokens, title, body):
    registration_ids = tokens 
    message_title = title 
    message_body = body
    push_service.notify_multiple_devices(registration_ids=registration_ids, message_title=message_title, message_body=message_body,click_action="http://localhost:3000/" )
