from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import AutorModel
from sqlalchemy import func, desc

#AUTORES = {
#    1: {
#        'id_autor': '1',
#        'id_libro': '1',
#        'nombre': 'Pedro Pascal'
#    },
#    2: {
#        'id_autor': '2',
#        'id_libro': '2',
#        'nombre': 'Leonardo Davinci'
#    },
#}

class Autor(Resource):
    def get(self, id):
        autor =db.session.query(AutorModel).get_or_404(id)
        return autor.to_json()
#        if int(id) in AUTORES:
  #          return AUTORES[int(id)]
    #    return 'No existe el id', 404
    
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


        #autores = db.session.query(AutorModel).all()
        #return jsonify([autor.to_json() for autor in autores])
    #    return AUTORES
    
    def post(self):
        autor = AutorModel.from_json(request.get_json())
        db.session.add(autor)
        db.session.commit()
        return autor.to_json(), 201
    #    Valoracion = request.get_json()
    #    id = int(max(AUTORES.keys())) + 1
    #    AUTORES[id] = Valoracion
    #    return AUTORES[id], 201