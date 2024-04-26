from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import LibroModel

#LIBROS = {

#    1: {
#        'titulo': 'Python',
#        'autor': '<NAME>'
#    },
#    2: {
#        'titulo': 'C++',
#        'autor': '<NAME>'
#    },
#    3: {
#        'titulo': 'Java',
#        'autor': '<NAME>'
#    },
#}

class Libro(Resource):
    def get(self, id):
        libro = db.session.query(LibroModel).get_or_404(id)
        return libro.to_json_complete()
    #    if int(id) in LIBROS:
    #        return LIBROS[int(id)]
    #    return 'No existe el id', 404

    def delete(self, id):
        libro = db.session.query(LibroModel).get_or_404(id)
        db.session.delete(libro)
        db.session.commit()
        return libro.to_json(), 204
    #    if int(id) in LIBROS:
    #        del LIBROS[int(id)]
    #        return '', 204
    #    return 'No existe el id', 404

    def put(self, id):
        libro = db.session.query(LibroModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(libro, key, value)
        db.session.add(libro)
        db.session.commit()
        return libro.to_json() , 201
    #    if int(id) in LIBROS:
    #        Libro = LIBROS[int(id)]
    #        data = request.get_json()
    #        Libro.update(data)
    #        return "", 201
    #    return "No existe el id", 404

class Libros(Resource):
    def get(self):
        libros = db.session.query(LibroModel).all()
        return jsonify([libro.to_json() for libro in libros])
    #    return LIBROS
    
    def post(self):
        libro = LibroModel.from_json(request.get_json())
        db.session.add(libro)
        db.session.commit()
        return libro.to_json(), 201

    #    Libro = request.get_json()
    #    id = int(max(LIBROS.keys())) + 1
    #    LIBROS[id] = Libro
    #    return LIBROS[id], 201