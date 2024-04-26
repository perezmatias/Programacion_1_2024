from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import UsuarioModel

#USUARIOS = {
#    1: {
#        'nombre': 'Juan',
#        'apellidos': 'Pérez',
#        'edad': 25
#    },
#    2: {
#        'nombre': 'Pedro',
#        'apellidos': 'Pérez',
#        'edad': 25
#    },
#    3: {
#        'nombre': 'Jose',
#        'apellidos': 'Pérez',
#        'edad': 25
#    }
#}

class Usuario(Resource):
    def get(self, id):
        usuario = db.session.query(UsuarioModel).get_or_404(id)
        return usuario.to_json_complete()
    #    if int(id) in USUARIOS:
    #        return USUARIOS[int(id)]
    #    return 'No existe el id', 404

    def delete(self, id):
        usuario = db.session.query(UsuarioModel).get_or_404(id)
        db.session.delete(usuario)
        db.session.commit()
        return usuario.to_json(), 204
    #    if int(id) in USUARIOS:
    #        del USUARIOS[int(id)]
    #        return '', 204
    #    return 'No existe el id', 404

    def put(self, id):
        usuario = db.session.query(UsuarioModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(usuario, key, value)
        db.session.add(usuario)
        db.session.commit()
        return usuario.to_json() , 201

    #    if int(id) in USUARIOS:
    #        Usuario=USUARIOS[int(id)]
    #        data = request.get_json()
    #        Usuario.update(data)
    #        return "", 201
    #    return "No existe el id", 404

class Usuarios(Resource):
    def get(self):
        usuarios = db.session.query(UsuarioModel).all()
        return jsonify([usuario.to_json() for usuario in usuarios])
    #    return USUARIOS
    
    def post(self):
        usuario = UsuarioModel.from_json(request.get_json())
        db.session.add(usuario)
        db.session.commit()
        return usuario.to_json(), 201
    #    Usuario = request.get_json()
    #    id = int(max(USUARIOS.keys())) + 1
    #    USUARIOS[id] = Usuario
    #    return USUARIOS[id], 201