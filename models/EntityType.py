from store.db_init import db
import enum
from sqlalchemy import func, Enum

class Entities(enum.Enum):
	user=1
	oferta_laboral=2
	necesidad_egresados=3
	
class EntityType(db.Model):
	__tablename__ = 'entity_type'
	id = db.Column(db.Integer, primary_key=True)
	entity = db.Column(db.Enum(Entities))
	description = db.Column(db.Text)

	@classmethod
	def get_by_id(self, id):
		entity_type= EntityType.query.filter_by(id=id).first()
		return entity_type
