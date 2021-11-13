from flask_migrate import Migrate
from routes.user_bp import user_bp
from models.User import User
from store.db_init import db
from store.jwt_init import guard
from store.app_store import app
import flask_cors

cors=flask_cors.CORS()


app.config.from_object('config')

db.init_app(app)

guard.init_app(app, User)

cors.init_app(app)

migrate = Migrate(app, db, compare_type=True)


#Add the admin user 
"""
with app.app_context():
    if db.session.query(User).filter_by(username='eliana').count() < 1:
        db.session.add(User(
          username='eliana',
          password=guard.hash_password('eliana'),
          roles='admin'
            ))
    db.session.commit()
"""

@app.route('/api/')
def index():
  return {"Hello": "World"}, 200


app.register_blueprint(user_bp, url_prefix='/api/users')




if __name__ == '__main__':
    #app.debug = True
    app.run()
