from src.app.models.user import User
from src.main import app
from flask import jsonify, request
from src.config.locales import language as lang


@app.route('/user/<int:uid>', methods=['GET'])
def user(uid):
    user = User.search_uid(uid)
    if user:
        return jsonify(user.to_json()), 200
    return lang.msg("not_found"), 404


@app.route('/user/', methods=['GET'])
def users():
    users = User.search_all()
    if users:
        return jsonify([
            user.to_json()
            for user in users
        ]), 200
    return lang.msg("not_found"), 404


@app.route('/user/', methods=['POST'])
def save():
    user = User.json_2_obj(request.get_json())
    resp = user.save()
    if resp:
        return jsonify(resp.to_json()), 200
    return lang.msg("save_fail"), 500


@app.route('/user/<int:uid>', methods=['DELETE'])
def delete(uid):
    user = User.delete(uid)
    if user:
        return jsonify(user.to_json()), 200
    return lang.msg("not_found"), 404