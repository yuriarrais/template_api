from src.app.models.user import User
from src.main import app
from flask import jsonify, request
from src.app.helpers.constants import no_content


@app.route('/user/<int:uid>', methods=['GET'])
def search_user(uid):
    try:
        user = User.search_uid(uid)
        return (jsonify(user.to_json()), 200) \
            if user else no_content(204)
    except Exception as e:
        return f'Cod: {type(e).__name__}\nMsg: {e}'


@app.route('/user/', methods=['GET'])
def search_users():
    try:
        users = User.search_all()
        return jsonify([
                user.to_json()
                for user in users
            ]), 200 \
            if users else no_content(204)
    except Exception as e:
        return f'Cod: {type(e).__name__}\nMsg: {e}'


@app.route('/user/', methods=['POST'])
def save():
    try:
        user = User.json_2_obj(request.get_json())
        resp = user.save()
        return jsonify(resp.to_json()), 200
    except Exception as e:
        return f'Cod: {type(e).__name__}\nMsg: {e}'


@app.route('/user/<int:uid>', methods=['DELETE'])
def delete(uid):
    try:
        user = User.delete(uid)
        return jsonify(user.to_json()), 200 \
            if user else no_content(204)
    except Exception as e:
        return f'Cod: {type(e).__name__}\nMsg: {e}'
