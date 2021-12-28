import os

#SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
# Enable debug mode.
DEBUG = True
# Connect to the database
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:adMin#12@localhost/notinorn?charset=utf8mb4'
#SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://bedf1554ecbeb8:e6f6d2e8@us-cdbr-east-04.cleardb.com/heroku_d16712f7edb2a95' 
#mysql://bedf1554ecbeb8:e6f6d2e8@us-cdbr-east-04.cleardb.com/heroku_d16712f7edb2a95?reconnect=true
# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False

#setup de jwt, tiempo,key ...
SECRET_KEY = "top_secret"
JWT_ACCESS_LIFESPAN = {'hours': 24}
JWT_REFRESH_LIFESPAN = {'days': 30}

#subir archivos al servidor
UPLOAD_FOLDER='static/uploads/'
MAX_CONTENT_LENGTH = 16 * 1024 * 1024