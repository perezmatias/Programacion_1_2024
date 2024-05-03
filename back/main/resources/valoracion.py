from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import ValoracionModel
from sqlalchemy import func, desc

class Valoracion(Resource):
    def get(self, id):
        valoracion = db.session.query(ValoracionModel).get_or_404(id)
        return valoracion.to_json()
    
class Valoraciones(Resource):
    def get(self):
        page = 1
        per_page = 10
        valoraciones = db.session.query(ValoracionModel)
        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))
        valoraciones = valoraciones.paginate(page=page, per_page=per_page, error_out=True)

        return jsonify({'valoraciones': [valoracion.to_json() for valoracion in valoraciones],
                        'total': valoraciones.total,
                        'pages': valoraciones.pages,
                        'page': page
                    })
    
    def post(self):
        valoracion = ValoracionModel.from_json(request.get_json())
        db.session.add(valoracion)
        db.session.commit()
        return valoracion.to_json(), 201
    