from flask_restful import Resource
from flask import request

COMENTARIOS = {
    '1': {
        'id_usuario': '1',
        'id_libro': '1',
        'comentario': 'Muy buen libro'
    },
    '2': {
        'id_usuario': '2',
        'id_libro': '2',
        'comentario': 'Muy buen libro'
    },
    '3': {
        'id_usuario': '3',
        'id_libro': '3',
        'comentario': 'Muy buen libro'
    }
}

class Comentario(Resource):
    def get(self, id):
        if int(id) in COMENTARIOS:
            return COMENTARIOS[int(id)]
        return 'No existe el id', 404
    
    def post(self):
        data = request.get_json()
        COMENTARIOS.update(data)
        id = int(max(COMENTARIOS.keys())) + 1
        COMENTARIOS[id] = Comentario
        return COMENTARIOS[id], 201