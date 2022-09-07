from flask import Blueprint
from flask import jsonify, request

users_bp = Blueprint("users", __name__, url_prefix="/users")


@users_bp.route("", methods=["GET"])
def get_all_users():
    all_users = [{"id": 1, "name": "bob"}, {"id": 2, "name": "joe"}]
    return jsonify(all_users)


@users_bp.route("", methods=["POST"])
def create_user():
    # request.data|.headers|.method|.files|.args
    d = request.json

    # option 1: return Response(status code) -> No body
    # option 2: return body, status code
    return jsonify(d), 201
