from store.db_init import db
	
class UserProfile(db.Model):
	__tablename__ = 'user_profile'
	id = db.Column(db.Integer, primary_key=True)
	user_id= db.Column(db.Integer, db.ForeignKey('user.id'), unique=True)
	full_name= db.Column(db.String(length=255))
	img = db.Column(db.Text())
	phone = db.Column(db.String(length=45))
	mobile = db.Column(db.String(length=45))
	address = db.Column(db.Text())
	web_site = db.Column(db.Text())
	github = db.Column(db.Text())
	twitter = db.Column(db.Text())
	facebook = db.Column(db.Text())

	def json(self):
		return {
			'id':self.id, 'user_id':self.user_id,
			'full_name':self.full_name,'img':self.img, 'phone':self.phone,
			'mobile':self.mobile, 'address':self.address,
			'web_site':self.web_site, 'github':self.github,
			'twitter':self.twitter, 'facebook':self.facebook
		}

	@classmethod 
	def save(self, user_id, full_name, img, phone, mobile, address, web_site, github, twitter, facebook):
		new_user_profile=UserProfile(
			user_id=user_id,
			full_name=full_name,
			img=img,
			phone=phone,
			mobile=mobile,
			address=address,
			web_site=web_site,
			github=github,
			twitter=twitter,
			facebook=facebook
			)
		db.session.add(new_user_profile)
		db.session.commit()
		return new_user_profile 


	@classmethod
	def update(self, user_id, full_name, img, phone, mobile, address, web_site, github, twitter, facebook):
		user_profile = UserProfile.query.filter_by(user_id=user_id).first()
		user_profile.full_name=full_name
		user_profile.img=img
		user_profile.phone=phone
		user_profile.mobile=mobile
		user_profile.address=address
		user_profile.web_site=web_site
		user_profile.github=github
		user_profile.twitter=twitter
		user_profile.facebook=facebook
		db.session.commit()
		return user_profile 

	@classmethod
	def get(self, user_id):
		user_profile = UserProfile.query.filter_by(user_id=user_id).first()
		return user_profile 

	@classmethod
	def delete(self, user_id):
		user_profile = UserProfile.query.filter_by(user_id=user_id).delete()
		db.session.commit()
		return user_profile 