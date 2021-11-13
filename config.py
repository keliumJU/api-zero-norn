import os

SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))
# Enable debug mode.
DEBUG = True
# Connect to the database
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/notinorn?charset=utf8mb4'
# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False

#setup de jwt, tiempo,key ...
#SECRET_KEY = "CHANGE_PATH_OF_SECRED_KEY"
JWT_ACCESS_LIFESPAN = {'hours': 24}
JWT_REFRESH_LIFESPAN = {'days': 30}

#subir archivos al servidor
UPLOAD_FOLDER='static/uploads/'
MAX_CONTENT_LENGTH = 16 * 1024 * 1024