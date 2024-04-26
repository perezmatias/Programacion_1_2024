from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import Autores_librosModel

class Autores_libros(Resource):
    def post(self):
        id_autor = request.get_json().get('id_autor')
        id_libro = request.get_json().get('id_libro')
        if id_autor is None:
            print("Autor no encontrado")
        if id_libro is None:
            print("Libro no encontrado")

        query = Autores_librosModel.insert().values(id_autor=id_autor, id_libro=id_libro)
        try:
            db.session.execute(query)
            db.session.commit()
        except:
            return 'Formato no correcto', 400
        return 'Creado con exito', 201