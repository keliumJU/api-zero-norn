from flask import Blueprint

from controllers.LaboralCategoryController import index, store, show, update, delete, getAll

category_laboral = Blueprint('category_laboral', __name__)

category_laboral.route('/all', methods=['GET'])(getAll)
category_laboral.route('/page', methods=['POST'])(index)
category_laboral.route('/create', methods=['POST'])(store)
category_laboral.route('/<int:laboral_category_id>', methods=['GET'])(show)
category_laboral.route('/<int:laboral_category_id>/edit', methods=['PUT'])(update)
category_laboral.route('/<int:laboral_category_id>', methods=['DELETE'])(delete)

