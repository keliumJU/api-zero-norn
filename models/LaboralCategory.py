from sqlalchemy.sql.expression import desc
from store.db_init import db

class LaboralCategory(db.Model):
    __tablename__ = 'laboral_category'
    id = db.Column(db.Integer, primary_key=True)
	#it's posible that this column have a attribute unique
    name = db.Column(db.Text())
    description = db.Column(db.Text())

    def json(self):
        return {
            'id':self.id, 'name':self.name,
            'description':self.description,        
		}
	
    @classmethod
    def get_all(self):
        laboral_categories=LaboralCategory.query.all()
        return laboral_categories


    @classmethod
    def get_by_page(self, search=None, ini=0, end=None):
        if(search==None):
            query = LaboralCategory.query. \
            offset(ini). \
            limit(end). \
            all()
        
        else:
            condition = db.or_(*[getattr(LaboralCategory, col).ilike(f'{val}%') for col, val in search.items()])
            query=LaboralCategory.query.filter(condition).offset(ini).limit(end).all()

        return query

    @classmethod 
    def save(self, name, description):
        new_laboral_category=LaboralCategory(
            name=name,
            description=description,
            )
        db.session.add(new_laboral_category)
        db.session.commit()
        return new_laboral_category 
    
    @classmethod
    def update(self, id, name, description):
        laboral_category= LaboralCategory.query.filter_by(id=id).first()
        laboral_category.name=name
        laboral_category.description=description
        db.session.commit()
        return laboral_category

    @classmethod
    def get(self, id):
        laboral_category = LaboralCategory.query.filter_by(id=id).first()
        return laboral_category
    
    @classmethod
    def delete(self, id):
        laboral_category = LaboralCategory.query.filter_by(id=id).delete()
        db.session.commit()
        return laboral_category