from sqlalchemy.orm import query
from store.db_init import db
import sqlalchemy as sa

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.Text())
    email = db.Column(db.String(100), unique=True, default=True, server_default='example@gmail.com')
    roles = db.Column(db.Text())
    is_active = db.Column(db.Boolean(), default=True, server_default='0')
    token_fcm = db.Column(db.Text()) 
    #El toquen debe ser unico ... sin embargo como no entamos en produccion no tendra el atributo unique, sin embargo, antes de subirse a produccion debera
    #agregarse este atributo "unique=True"

    def json(self):
        return {
            'id':self.id, 'username':self.username,
            'password':self.password, 'email':self.email,
            'roles':self.roles, 'is_active':self.is_active,
            'token_fcm':self.token_fcm 
        }

    @property
    def rolenames(self):
        try:
            return self.roles.split(',')
        except Exception:
            return []

    @classmethod
    def lookup(cls, username):
        return cls.query.filter_by(username=username).one_or_none()

    @classmethod
    def identify(cls, id):
        return cls.query.get(id)

    @property
    def identity(self):
        return self.id

    def is_valid(self):
        return self.is_active
        
    @classmethod 
    def save(self, username, password, email, roles, is_active, token_fcm):
        new_user=User(
            username=username,
            password=password,
            email=email,
            roles=roles,
            is_active=is_active,
            token_fcm=token_fcm
            )
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @classmethod 
    def find_by_username(self, username):
        user = User.query.filter_by(username=username).first()
        return user 

    @classmethod 
    def find_by_id(self, id):
        user = User.query.filter_by(id=id).first()
        return user 
    
    @classmethod 
    def find_by_email(self, email):
        user = User.query.filter_by(email=email).first()
        return user

    @classmethod
    def get_by_page(self, search=None, ini=0, end=None):
        if(search==None):
            print("here")
            query = User.query. \
            offset(ini). \
            limit(end). \
            all()
        
        else:
            condition = db.or_(*[getattr(User, col).ilike(f'{val}%') for col, val in search.items()])
            query=User.query.filter(condition).offset(ini).limit(end).all()

        return query

    #profile
    @classmethod
    def update(self, id, username, password, email, roles):
        user = User.query.filter_by(id=id).first()
        user.username=username
        user.passowrd=password
        user.email=email
        user.roles=roles
        db.session.commit()
        return user

    #admin    
    @classmethod
    def activate_user(self, id):
        user = User.query.filter_by(id=id).first()
        if(user.is_active):
            user.is_active=False
        else:
            user.is_active=True 

        db.session.commit()
        return user

    @classmethod
    def get(self, id):
        user = User.query.filter_by(id=id).first()
        return user
    
    @classmethod
    def delete(self, id):
        user = User.query.filter_by(id=id).delete()
        db.session.commit()
        return user

    @classmethod
    def add_token_fcm(self, id, token_fcm):
        user = User.query.filter_by(id=id).first()
        user.token_fcm=token_fcm
        db.session.commit()
        return user

    @classmethod
    def get_tokens_by_list_ids(self, list_ids):
        list_of_tokens=[]
        for id_ in list_ids:
            user=User.query.filter_by(id=id_).first()
            list_of_tokens.append(user.token_fcm)
        return list_of_tokens