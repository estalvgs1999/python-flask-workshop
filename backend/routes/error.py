from flask import Blueprint
from flask import jsonify

from werkzeug.exceptions import NotFound

error_bp = Blueprint("error", __name__)


@error_bp.app_errorhandler(NotFound)
def handle_not_found(err):
    return jsonify({"message": "This resource isn't available."}), 404


@error_bp.app_errorhandler(Exception)
def handle_generic_exception(err):
    return jsonify({"message": "Unknown error. Please check the logs for more details."}), 500
