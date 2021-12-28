from typing import TYPE_CHECKING
from store.db_init import db
import enum
from sqlalchemy import func, Enum

class TypeOffer(enum.Enum):
	contrato=1
	prestaciones=2
	practica_empresarial=3
	
class JobOffer(db.Model):
	__tablename__ = 'job_offer'
	id = db.Column(db.Integer, primary_key=True)
	laboral_category_id = db.Column(db.Integer, db.ForeignKey('laboral_category.id'))
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	type_offer = db.Column(db.Enum(TypeOffer))
	salary = db.Column(db.Numeric())
	description = db.Column(db.Text())
	status = db.Column(db.Boolean())

	def json(self):
		return {
			'id':self.id, 'laboral_category_id':self.laboral_category_id,
			'user_id':self.user_id, 'type_offer':self.type_offer.name,
			'salary':str(self.salary), 'description':self.description,
			'status':self.status        
		}


	@classmethod
	def get_by_page(self,user_id, search=None, ini=0, end=None):
		if(search==None):
			query = JobOffer.query. \
            filter_by(user_id=user_id). \
			offset(ini). \
			limit(end). \
			all()
		
		else:
			condition = db.and_(*[getattr(JobOffer, col).ilike(f'{val}%') for col, val in search.items()])
			query=JobOffer.query.filter(JobOffer.user_id==user_id, condition).offset(ini).limit(end).all()

		return query

	@classmethod 
	def save(self, laboral_category_id, user_id, type_offer, salary, description, status):
		new_job_offer=JobOffer(
			laboral_category_id=laboral_category_id,
			user_id=user_id,
			type_offer=type_offer,
			salary=salary,
			description=description,
			status=status
			)
		db.session.add(new_job_offer)
		db.session.commit()
		return new_job_offer 


	@classmethod
	def update(self,id, laboral_category_id, user_id, type_offer, salary, description, status):
		job_offer = JobOffer.query.filter_by(id=id).first()
		job_offer.laboral_category_id=laboral_category_id
		job_offer.user_id=user_id
		job_offer.type_offer=type_offer
		job_offer.salary=salary
		job_offer.description=description
		job_offer.status=status
		db.session.commit()
		return job_offer 

	@classmethod
	def get(self, id):
		job_offer = JobOffer.query.filter_by(id=id).first()
		return job_offer 

	@classmethod
	def delete(self, id):
		job_offer = JobOffer.query.filter_by(id=id).delete()
		db.session.commit()
		return job_offer 

	@classmethod
	def find_by_laboral_category_active(self, laboral_category_id):
		job_offers=JobOffer.query.filter_by(laboral_category_id=laboral_category_id, status=True).group_by(JobOffer.user_id).all()
		return job_offers 