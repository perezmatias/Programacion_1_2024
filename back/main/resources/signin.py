from flask_restful import Resource
from flask import request

#SIGNIN={
#    1: {
#        'username': 'admin',
#        'rol': 'admin',
#        'password': 'admin'
#    },
#    2: {
#        'username': 'user',
#        'rol': 'user',
#        'password': 'user'
#    },
#}

class Signin(Resource):
    def post(self):
        Signin = request.get_json()
        id = int(max(SIGNIN.keys())) + 1
        SIGNIN[id] = Signin
        return SIGNIN[id], 201