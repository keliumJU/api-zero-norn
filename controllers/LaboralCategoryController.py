from flask import json, request, make_response, jsonify
from sqlalchemy.sql.expression import desc
from models.LaboralCategory import LaboralCategory 

#Notification system model
from models.EntityType import EntityType

#helpers
from helper.helper import *

from store.jwt_init import guard, flask_praetorian


LIMIT_PAGE=10


def getAll():
    laboral_categories=LaboralCategory.get_all()
    return jsonify([LaboralCategory.json(category) for category in laboral_categories])


@flask_praetorian.roles_accepted("admin", "graduate","company")
def index():
	req=request.get_json(force=True)
	search=req.get('search', None)
	page_number = req.get('page_number', None)

	page=LaboralCategory.get_by_page(
		search=search, 
		ini=page_number*LIMIT_PAGE,
		end=LIMIT_PAGE
		)
	return make_response(jsonify([LaboralCategory.json(category) for category in page]),200)

@flask_praetorian.roles_accepted("admin", "graduate","company")
def store():
    name=request.form.get('name',None)
    description=request.form.get('description',None)

    laboral_category = LaboralCategory.save(
        name=name,
        description=description,
        )

    if(laboral_category):
        return make_response(jsonify({"msg":"Categoria laboral creada satisfactoriamente"}), 200)
    else:
        return make_response(jsonify({"error":"Se produjo un error al crear la categoria laboral"}), 400)

@flask_praetorian.roles_accepted("admin", "graduate","company")
def show(laboral_category_id):
    laboral_category=LaboralCategory.get(laboral_category_id)
    if(laboral_category):
        return make_response(jsonify({"laboral_category": LaboralCategory.json(laboral_category)},200))
    else:
        return make_response(jsonify({"msg":"Sucedio un error al mostrar la categoria laboral"},400))

@flask_praetorian.roles_required("admin")
def update(laboral_category_id):
    name=request.form.get('name',None)
    description=request.form.get('description',None)

    laboral_category = LaboralCategory.update(
        id=laboral_category_id,
        name=name,
        description=description,
        )
    if(laboral_category):
        return make_response(jsonify({"msg":"Categoria laboral actualizada satisfactoriamente"}, 200))
    else:
        return make_response(jsonify({"error":"Se produjo un error al actualizar la categoria laboral"}), 400)

@flask_praetorian.roles_required("admin")
def delete(laboral_category_id):
    laboral_category=LaboralCategory.delete(laboral_category_id)
    if(laboral_category):
        return make_response(jsonify({"msg":"Categoria laboral eliminado correctamente"}, 200))
    else:
        return make_response(jsonify({"msg":"Sucedio un error al eliminar la categoria laboral"}), 400)