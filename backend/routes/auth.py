from flask import Blueprint, request
from werkzeug.security import check_password_hash

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["POST"])
def login():
    req = request.json

    if "username" not in req or "password" not in req:
        raise Exception("Unable to authenticate")

    if not check_password_hash(
        allowed_users[req["username"]],
        req["password"]
    ):
        pass
