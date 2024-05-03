from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import NotificacionModel
from sqlalchemy import func, desc

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
    
    def get(self):
        page = 1
        per_page =10
        notificaciones = db.session.query(NotificacionModel)
        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))
        notificaciones = notificaciones.paginate(page=page, per_page=per_page, error_out=True)
        return jsonify({'notificaciones': [notificacion.to_json() for notificacion in notificaciones],
                  'total': notificaciones.total,
                  'pages': notificaciones.pages,
                  'page': page
                })
        #notificaciones = db.session.query(NotificacionModel).all()
        #return jsonify([notificacion.to_json() for notificacion in notificaciones])
    #    Notificacion = request.get_json()
    #    id = int(max(NOTIFICACIONES.keys())) + 1
    #    NOTIFICACIONES[id] = Notificacion
    #    return NOTIFICACIONES[id], 201