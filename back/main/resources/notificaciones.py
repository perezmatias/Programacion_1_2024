from flask_restful import Resource
from flask import request

NOTIFICACIONES = {
    '1': {
        'id_usuario': '1',
        'mensaje': 'Tiene un libro vencido'
    },
    '2': {
        'id_usuario': '2',
        'mensaje': 'Tiene un libro vencido'
    },
    '3': {
        'id_usuario': '3',
        'mensaje': 'Tiene un libro vencido'
    }
}

class Notificacion(Resource):
    def post(self):
        data = request.get_json()
        NOTIFICACIONES.update(data)
        id = int(max(NOTIFICACIONES.keys())) + 1
        NOTIFICACIONES[id] = Notificacion
        return NOTIFICACIONES[id], 201