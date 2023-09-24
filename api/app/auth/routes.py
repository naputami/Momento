from flask import jsonify, request
from app.extentions import db, jwt
from app.models.user import Users
from app.models.blacklist_token import BlacklistTokens
from app.auth import authBp
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt, get_jwt_identity

@authBp.route("/signup", methods = ['POST'], strict_slashes = False)
def sign_up():
    data = request.get_json()
    name = data.get("name", None)
    email = data.get("email", None)
    username = data.get("username", None)
    role = data.get("role", "user")
    password_hash = generate_password_hash(data.get("password", None))

    if not name or not email or not password_hash or not username:
        return jsonify({
        "message": "Name, email, username, and password are required"
    }), 400

    try:
        db.session.add(Users(
            name=name,
            username=username,
            email=email,
            password_hash=password_hash,
            role=role
        ))
        db.session.commit()
    except IntegrityError:
        return jsonify({
            "message": "email or username is already registered"
        }), 422

    return jsonify({
        "message": "Registration user is completed"
    }), 200

@authBp.route("/login", methods=["POST"], strict_slashes = False)
def login():
    data = request.get_json()

    username =data.get("username", None)
    password = data.get("password", None)

    if not username or not password:
        return jsonify({
            "message": "username and password are required"
        }), 400
    
    user = Users.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password_hash, password):
        return jsonify({
            "message": "Username or password is invalid"
        }), 400
    
    access_token = create_access_token(identity=user.id)
    refresh_token = create_refresh_token(identity=user.id)

    return jsonify({
        "message": "Login success",
        "accessToken": access_token,
        "refreshToken": refresh_token
    }), 200

@authBp.route("/logout", methods=["POST"], strict_slashes = False)
@jwt_required(locations=["headers"])
def logout():
    raw_jwt = get_jwt()

    jti = raw_jwt.get("jti")

    token = BlacklistTokens(jti=jti)

    db.session.add(token)
    db.session.commit()

    return jsonify({
        "message": "Logged out sucessfully"
    }), 200

@authBp.route("/refresh", methods = ['POST'], strict_slashes = False)
@jwt_required(refresh=True)
def refresh():
    current_user = get_jwt_identity()
    access_token = {
        'access token': create_access_token(identity=current_user)
    }
    return jsonify(access_token), 200


@jwt.token_in_blocklist_loader
def check_if_token_is_revoked(jwt_header, jwt_payload: dict):
    jti = jwt_payload["jti"]
    token = BlacklistTokens.query.filter_by(jti=jti).first()
    return token is not None



    