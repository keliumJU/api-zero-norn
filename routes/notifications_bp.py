from flask import Blueprint

from controllers.NotificationController import get_notifications_by_user_page, delete_notification, revised_notification

notifications_bp = Blueprint('notifications_bp', __name__)
notifications_bp.route('/', methods=['POST'])(get_notifications_by_user_page)
notifications_bp.route('/delete', methods=['DELETE'])(delete_notification)
notifications_bp.route('/revised', methods=['POST'])(revised_notification)