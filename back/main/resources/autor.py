from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import AutorModel
from sqlalchemy import func, desc


class Autor(Resource):
    def get(self, id):
        autor =db.session.query(AutorModel).get_or_404(id)
        return autor.to_json()
    
class Autores(Resource):
    def get(self):
        page = 1
        per_page = 10
        autores = db.session.query(AutorModel)
        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))
        
        if request.args.get('nombre'):
            autores=autores.filter(AutorModel.nombre.like("%"+request.args.get('nombre')+"%"))
        
        if request.args.get('sortby_nombre'):
            autores=autores.order_by(desc(AutorModel.nombre))

        if request.args.get('apellido'):
            autores=autores.filter(AutorModel.apellido.like("%"+request.args.get('apellido')+"%"))
        
        if request.args.get('sortby_apellido'):
            autores=autores.order_by(desc(AutorModel.apellido))
        
        autores = autores.paginate(page=page, per_page=per_page, error_out=True)
        return jsonify({'autores':[autor.to_json() for autor in autores],
                        'total': autores.total,
                        'pages': autores.pages,
                        'page': page
                    })
    
    def post(self):
        autor = AutorModel.from_json(request.get_json())
        db.session.add(autor)
        db.session.commit()
        return autor.to_json(), 201