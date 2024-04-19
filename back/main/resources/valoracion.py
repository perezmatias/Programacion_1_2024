from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import ValoracionModel

#VALORACIONES = {
#    1: {
#        'id_usuario': '1',
#        'id_libro': '1',
#        'valoracion': '5'
#    },
#    2: {
#        'id_usuario': '2',
#        'id_libro': '2',
#        'valoracion': '4'
#    },
#    3: {
#        'id_usuario': '3',
#        'id_libro': '3',
#        'valoracion': '3'
#    }
#}

class Valoracion(Resource):
    def get(self, id):
        valoracion = db.session.query(ValoracionModel).get_or_404(id)
        return valoracion.to_json()
    #    if int(id) in VALORACIONES:
    #        return VALORACIONES[int(id)]
    #    return 'No existe el id', 404
    
class Valoraciones(Resource):
    def get(self):
        valoraciones = db.session.query(ValoracionModel).all()
        return jsonify([valoracion.to_json() for valoracion in valoraciones])
    #    return VALORACIONES
    
    def post(self):
        valoracion = ValoracionModel.from_json(request.get_json())
        db.session.add(valoracion)
        db.session.commit()
        return valoracion.to_json(), 201
    #    Valoracion = request.get_json()
    #    id = int(max(VALORACIONES.keys())) + 1
    #    VALORACIONES[id] = Valoracion
    #    return VALORACIONES[id], 201