
from flask.signals import message_flashed


class NotificationDetails():
	def __init__(self, object_id, entity_id, entity_type_id, notifier_id, created_on, message, img_user, status):
		self.object_id=object_id
		self.entity_id=entity_id
		self.entity_type_id=entity_type_id
		self.notifier_id=notifier_id
		self.message=message
		self.img_user=img_user
		self.created_on=created_on
		self.status=status

	def json(self):
		return {
			'id':self.object_id, 'entity_id':self.entity_id,
			'entity_type_id':self.entity_type_id, 'notifier_id':self.notifier_id,
			'created_on':self.created_on, 'message':self.message, 'img_user':self.img_user, 'status':self.status
		}

