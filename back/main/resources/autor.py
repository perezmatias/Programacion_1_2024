from flask_restful import Resource
from flask import request

AUTORES = {
    1: {
        'id_autor': '1',
        'id_libro': '1',
        'nombre': 'Pedro Pascal'
    },
    2: {
        'id_autor': '2',
        'id_libro': '2',
        'nombre': 'Leonardo Davinci'
    },
}

class Autor(Resource):
    def get(self, id):
        if int(id) in AUTORES:
            return AUTORES[int(id)]
        return 'No existe el id', 404
    
class Autores(Resource):
    def get(self):
        return AUTORES
    
    def post(self):
        Valoracion = request.get_json()
        id = int(max(AUTORES.keys())) + 1
        AUTORES[id] = Valoracion
        return AUTORES[id], 201