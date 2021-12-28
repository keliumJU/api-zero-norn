from flask import Blueprint

from controllers.UserProfileController import index, store,update, delete 

user_profile_bp = Blueprint('user_profile_bp', __name__)
user_profile_bp.route('/<int:user_id>', methods=['GET'])(index)
user_profile_bp.route('/create', methods=['POST'])(store)
user_profile_bp.route('/<int:user_id>/edit', methods=['PUT'])(update)
user_profile_bp.route('/<int:user_id>', methods=['DELETE'])(delete)


