from flask_restful import Resource
from flask import request

USUARIOS = {
    1: {
        'nombre': 'Juan',
        'apellidos': 'Pérez',
        'edad': 25
    },
    2: {
        'nombre': 'Pedro',
        'apellidos': 'Pérez',
        'edad': 25
    },
    3: {
        'nombre': 'Jose',
        'apellidos': 'Pérez',
        'edad': 25
    }
}

class Usuario(Resource):
    def get(self, id):
        if int(id) in USUARIOS:
            return USUARIOS[int(id)]
        return 'No existe el id', 404

    def delete(self, id):
        if int(id) in USUARIOS:
            del USUARIOS[int(id)]
            return '', 204
        return 'No existe el id', 404

    def put(self, id):
        if int(id) in USUARIOS:
            Usuario=USUARIOS[int(id)]
            data = request.get_json()
            Usuario.update(data)
            return "", 201
        return "No existe el id", 404

class Usuarios(Resource):
    def get(self):
        return USUARIOS
    
    def post(self):
        Usuario = request.get_json()
        id = int(max(USUARIOS.keys())) + 1
        USUARIOS[id] = Usuario
        return USUARIOS[id], 201