from sqlalchemy.orm import query
from store.db_init import db
import sqlalchemy as sa

class Notification(db.Model):
    __tablename__ = 'notification'
    id = db.Column(db.Integer, primary_key=True)
    notification_object_id = db.Column(db.Integer, db.ForeignKey('notification_object.id'))
    notifier_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    status = db.Column(db.Boolean())


    @classmethod
    def save_data(self, notification_object_id, notifier_id, status):
        new_notification=Notification(
            notification_object_id=notification_object_id,
            notifier_id=notifier_id,
            status=status
        )
        db.session.add(new_notification)
        db.session.commit()
        return new_notification
    #notifiers in base notification_object_id

    @classmethod
    def get_notifiers(self, notification_object_id):
        notifiers=Notification.query.filter_by(notification_object_id=notification_object_id).all()
        return notifiers
    
    @classmethod
    def delete_notifcation(self, notifier_id, notification_object_id):
        notification = Notification.query.filter_by(notifier_id=notifier_id, notification_object_id=notification_object_id).delete()
        db.session.commit()    
        return notification

    @classmethod
    def change_status(self, notifier_id, notification_object_id):
        notification = Notification.query.filter_by(notifier_id=notifier_id, notification_object_id=notification_object_id).first()
        notification.status=True 
        db.session.commit()    
        return notification 