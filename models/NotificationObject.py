from store.db_init import db
from sqlalchemy import func


class NotificationObject(db.Model):
	__tablename__ = 'notification_object'
	id = db.Column(db.Integer, primary_key=True)
	#How create the message in base the tables or modules
	entity_type_id = db.Column(db.Integer, db.ForeignKey('notification_object.id'))
	entity_id = db.Column(db.Integer)
	created_on = db.Column(db.DateTime(timezone=True), server_default=func.now())
	status = db.Column(db.Boolean())

	
	def json(self):
		return {
			'id':self.id, 'entity_type_id':self.entity_type_id,
			'entity_id':self.entity_id, 'created_on':self.created_on,
			'status':self.status
		}


	def __str__(self):
		return str({
			'id':self.id, 'entity_type_id':self.entity_type_id,
			'entity_id':self.entity_id, 'created_on':self.created_on,
			'status':self.status
		})

	@classmethod
	def save_data(self, entity_type_id, entity_id, status):
		new_notification_object=NotificationObject(
			entity_type_id=entity_type_id,
			entity_id=entity_id,
			status=status
		)
		db.session.add(new_notification_object)
		db.session.commit()
		return new_notification_object

