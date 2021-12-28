from flask import Blueprint

from controllers.JobOfferController import index, store, show, update, delete 

job_offer_bp = Blueprint('job_offer_bp', __name__)
job_offer_bp.route('/page', methods=['POST'])(index)
job_offer_bp.route('/create', methods=['POST'])(store)
job_offer_bp.route('/<int:job_offer_id>', methods=['GET'])(show)
job_offer_bp.route('/<int:job_offer_id>/edit', methods=['PUT'])(update)
job_offer_bp.route('/<int:job_offer_id>', methods=['DELETE'])(delete)


