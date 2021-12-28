from store.db_init import db
from sqlalchemy import func


class NotificationChange(db.Model):
	__tablename__ = 'notification_change'
	id = db.Column(db.Integer, primary_key=True)
	notification_object_id = db.Column(db.Integer, db.ForeignKey('notification_object.id'))
	actor_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	status = db.Column(db.Boolean())

	@classmethod
	def save_data(self, notification_object_id, actor_id, status):
		new_notification_change=NotificationChange(
			notification_object_id=notification_object_id,
			actor_id=actor_id,
			status=status
		)
		db.session.add(new_notification_change)
		db.session.commit()
		return new_notification_change

	@classmethod
	def get_by_object_id(self, object_id):
		notificationChange=NotificationChange.query.filter_by(notification_object_id=object_id).first()
		return notificationChange

	@classmethod
	def change_status(self, notifier_id, notification_object_id):
		notification = NotificationChange.query.filter_by(notifier_id=notifier_id, notification_object_id=notification_object_id).first()
		notification.status=True 
		db.session.commit()    
		return notification 