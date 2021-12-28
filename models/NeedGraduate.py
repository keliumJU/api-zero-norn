from store.db_init import db

class NeedGraduate(db.Model):
    __tablename__ = 'need_graduate'
    id = db.Column(db.Integer, primary_key=True)
    laboral_category_id = db.Column(db.Integer, db.ForeignKey('laboral_category.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    status = db.Column(db.Boolean())

    def json(self):
        return {
            'id':self.id, 'laboral_category_id':self.laboral_category_id,
            'user_id':self.user_id, 'status':self.status        
		}
	


    @classmethod
    def get_by_page(self, user_id, search=None, ini=0, end=None):
        if(search==None):
            query = NeedGraduate.query. \
            filter_by(user_id=user_id). \
            offset(ini). \
            limit(end). \
            all()
        
        else:
            condition = db.and_(*[getattr(NeedGraduate, col).ilike(f'{val}%') for col, val in search.items()])
            query=NeedGraduate.query.filter(NeedGraduate.user_id==user_id, condition).offset(ini).limit(end).all()

        return query



    @classmethod 
    def save(self, laboral_category_id, user_id, status):
        new_need_graduate=NeedGraduate(
            laboral_category_id=laboral_category_id,
            user_id=user_id,
            status=status
            )
        db.session.add(new_need_graduate)
        db.session.commit()
        return new_need_graduate 
    
    @classmethod
    def update(self, id, laboral_category_id, user_id, status):
        need_graduate= NeedGraduate.query.filter_by(id=id).first()
        need_graduate.laboral_category_id=laboral_category_id
        need_graduate.user_id = user_id 
        need_graduate.status = status 
        db.session.commit()
        return need_graduate 

    @classmethod
    def get(self, id):
        need_gradute = NeedGraduate.query.filter_by(id=id).first()
        return need_gradute 
    
    @classmethod
    def delete(self, id):
        need_graduate = NeedGraduate.query.filter_by(id=id).delete()
        db.session.commit()
        return need_graduate 

    @classmethod
    def find_by_laboral_category_active(self, laboral_category_id):
        need_graduates=NeedGraduate.query.filter_by(laboral_category_id=laboral_category_id, status=True).group_by(NeedGraduate.user_id).all()
        return need_graduates
    
    @classmethod
    def filter_by_category(self, laboral_category_id):
        need_graduates=NeedGraduate.query.filter_by(laboral_category_id=laboral_category_id).all()

