from flask import Blueprint

from controllers.UserController import index, store, show, update, delete, login, refresh, protected, get_page, active_user, logout_msg

user_bp = Blueprint('user_bp', __name__)
user_bp.route('/', methods=['GET'])(index)
user_bp.route('/create', methods=['POST'])(store)
user_bp.route('/<int:userId>', methods=['GET'])(show)
user_bp.route('/<int:userId>/edit', methods=['PUT'])(update)
user_bp.route('/<int:userId>', methods=['DELETE'])(delete)

#Auth user
user_bp.route('/login', methods=['POST'])(login)
user_bp.route('/logout', methods=['POST'])(logout_msg)
user_bp.route('/refresh', methods=['POST'])(refresh)
user_bp.route('/protected', methods=['GET'])(protected)

#Pagination user
user_bp.route('/page', methods=['POST'])(get_page)

#Active user
user_bp.route('/<int:userId>/active', methods=['GET'])(active_user)
