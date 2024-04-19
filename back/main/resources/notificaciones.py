from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import NotificacionModel

#NOTIFICACIONES = {
#    1: {
#        'id_usuario': '1',
#        'mensaje': 'Tiene un libro vencido'
#    },
#    2: {
#        'id_usuario': '2',
#        'mensaje': 'Tiene un libro vencido'
#    },
#    3: {
#        'id_usuario': '3',
#        'mensaje': 'Tiene un libro vencido'
#    }
#}

class Notificacion(Resource):
    def post(self):
        notificacion = NotificacionModel.from_json(request.get_json())
        db.session.add(notificacion)
        db.session.commit()
        return notificacion.to_json(), 201
    #    Notificacion = request.get_json()
    #    id = int(max(NOTIFICACIONES.keys())) + 1
    #    NOTIFICACIONES[id] = Notificacion
    #    return NOTIFICACIONES[id], 201