from flask_restful import Resource
from flask import request

VALORACIONES = {
    '1': {
        'id_usuario': '1',
        'id_libro': '1',
        'valoracion': '5'
    },
    '2': {
        'id_usuario': '2',
        'id_libro': '2',
        'valoracion': '4'
    },
    '3': {
        'id_usuario': '3',
        'id_libro': '3',
        'valoracion': '3'
    }
}

class Valoracion(Resource):
    def get(self, id):
        if int(id) in VALORACIONES:
            return VALORACIONES[int(id)]
        return 'No existe el id', 404
    
    def post(self):
        data = request.get_json()
        VALORACIONES.update(data)
        id = int(max(VALORACIONES.keys())) + 1
        VALORACIONES[id] = Valoracion
        return VALORACIONES[id], 201