from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import AutorModel

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
        autores = db.session.query(AutorModel).all()
        return jsonify([autor.to_json() for autor in autores])
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