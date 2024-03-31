from flask_restful import Resource
from flask import request

SIGNIN={

}

class Signin(Resource):
    def post(self):
        data = request.get_json()
        SIGNIN.update(data)
        id = int(max(SIGNIN.keys())) + 1
        SIGNIN[id] = Signin
        return SIGNIN[id], 201