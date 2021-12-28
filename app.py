from flask_migrate import Migrate
from helper.helper import notification_details_page


#BluePrints
from routes.user_bp import user_bp
from routes.notifications_bp import notifications_bp 
from routes.category_laboral import category_laboral
from routes.need_graduate_bp import need_graduate 
from routes.job_offer_bp import job_offer_bp 
from routes.user_profile_bp import user_profile_bp 

#My modelsk
from models.User import User
from models.UserProfile import UserProfile 


#sistem notification
from models.EntityType import EntityType 
from models.NotificationObject import NotificationObject 
from models.Notification import Notification 
from models.NotificationChange import NotificationChange 

#business logic
from models.JobOffer import JobOffer
from models.LaboralCategory import LaboralCategory
from models.NeedGraduate import NeedGraduate 


from store.db_init import db
from store.jwt_init import guard
from store.app_store import app
import flask_cors

from flask import jsonify, make_response

cors=flask_cors.CORS()

app.config.from_object('config')

guard.init_app(app, User)

db.init_app(app)

cors.init_app(app)

migrate = Migrate(app, db, compare_type=True)

#Add the admin user 

with app.app_context():
    if db.session.query(User).filter_by(username='eliana').count() < 1:
        db.session.add(User(
          username='eliana',
          password=guard.hash_password('eliana'),
          roles='admin'
            ))
    db.session.commit()

@app.route('/')
def index():
  return make_response(
    jsonify({"Hello": "World"}),
    200)


app.register_blueprint(user_bp, url_prefix='/api/users')
app.register_blueprint(notifications_bp, url_prefix='/api/notifications')
app.register_blueprint(notifications_bp, url_prefix='/api/notifications')
app.register_blueprint(category_laboral, url_prefix='/api/laboral_category')
app.register_blueprint(need_graduate, url_prefix='/api/need_graduate')
app.register_blueprint(job_offer_bp, url_prefix='/api/job_offer')
app.register_blueprint(user_profile_bp, url_prefix='/api/user_profile')


if __name__ == '__main__':
    app.debug = True
    app.run()
