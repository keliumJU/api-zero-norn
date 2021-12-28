from flask import Blueprint

from controllers.NeedGraduateController import index, store, show, update, delete 

need_graduate = Blueprint('need_graduate', __name__)
need_graduate.route('/page', methods=['POST'])(index)
need_graduate.route('/create', methods=['POST'])(store)
need_graduate.route('/<int:need_graduate_id>', methods=['GET'])(show)
need_graduate.route('/<int:need_graduate_id>/edit', methods=['PUT'])(update)
need_graduate.route('/<int:need_graduate_id>', methods=['DELETE'])(delete)


