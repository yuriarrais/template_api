from src.app.models.user import User
from src.main import app
from flask import jsonify, request
from src.app.helpers.constants import no_content


@app.route('/user/<int:uid>', methods=['GET'])
def search_user(uid):
    try:
        user = User.search_uid(uid)
        return response(user.to_json()) \
            if user else response({}, "Não existe nenhum usuário para o id solicitado.", "warning")
    except Exception as e:
        return response({}, f'{type(e).__name__} - {e}', "danger")


@app.route('/user/', methods=['GET'])
def search_users():
    try:
        users = User.search_all()
        return response([user.to_json() for user in users]) \
            if users else response({}, "Não existe nenhum usuário para ser exibido.", "warning")
    except Exception as e:
        return response({}, f'{type(e).__name__} - {e}', "danger")


@app.route('/user/', methods=['POST'])
def save():
    try:
        user = User.json_2_obj(request.json)
        resp = user.save()
        return response(resp.to_json(), "Usuário salvo com sucesso.")
    except Exception as e:
        return response({}, f'{type(e).__name__} - {e}', "danger")


@app.route('/user/<int:uid>', methods=['DELETE'])
def delete(uid):
    try:
        user = User.delete(uid)
        return response(user.to_json(), f'Usuário, {user.full_name}, deletado com sucesso.') \
            if user else response({}, f'Não foi possível deletar usuário. Usuário não existe.', "warning")
    except Exception as e:
        return response({}, f'{type(e).__name__} - {e}', "danger")


def response(user, msg="", type="success"):
    return jsonify({
        "obj": user,
        "msg": msg,
        "type": type
    })
