from flask_restful import Resource
from flask import request

LIBROS = {

    1: {
        'titulo': 'Python',
        'autor': '<NAME>'
    },
    2: {
        'titulo': 'C++',
        'autor': '<NAME>'
    },
    3: {
        'titulo': 'Java',
        'autor': '<NAME>'
    },
}

class Libro(Resource):
    def get(self, id):
        if int(id) in LIBROS:
            return LIBROS[int(id)]
        return 'No existe el id', 404

    def delete(self, id):
        if int(id) in LIBROS:
            del LIBROS[int(id)]
            return '', 204
        return 'No existe el id', 404

    def put(self, id):
        if int(id) in LIBROS:
            Libro = LIBROS[int(id)]
            data = request.get_json()
            Libro.update(data)
            return "", 201
        return "No existe el id", 404

class Libros(Resource):
    def get(self):
        return LIBROS
    
    def post(self):
        Libro = request.get_json()
        id = int(max(LIBROS.keys())) + 1
        LIBROS[id] = Libro
        return LIBROS[id], 201