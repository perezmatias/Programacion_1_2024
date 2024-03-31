from flask_restful import Resource
from flask import request

LOGIN={
    '1': {
        'username': 'admin',
        'password': 'admin'
    },
    '2': {
        'username': 'user',
        'password': 'user'
    },
}

class Login(Resource):
    def post(self):
        data = request.get_json()
        LOGIN.update(data)
        id = int(max(LOGIN.keys())) + 1
        LOGIN[id] = Login
        return LOGIN[id], 201
