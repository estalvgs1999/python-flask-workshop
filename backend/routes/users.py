from flask import Blueprint
from flask import jsonify, request
from backend.routes import basic_auth, token_auth

users_bp = Blueprint("users", __name__, url_prefix="/users")


@users_bp.route("", methods=["GET"])
@basic_auth.login_required
def get_all_users():
    all_users = [{"id": 1, "name": "bob"}, {"id": 2, "name": "joe"}]
    return jsonify(all_users)


@users_bp.route("", methods=["POST"])
@token_auth.login_required
def create_user():
    # request.data|.headers|.method|.files|.args
    d = request.json

    # option 1: return Response(status code) -> No body
    # option 2: return body, status code
    return jsonify(d), 201
