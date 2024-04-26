from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import Prestamos_librosModel

class Prestamos_libros(Resource):
    def post(self):
        id_libro = request.get_json().get('id_libro')
        id_prestamo = request.get_json().get('id_prestamo')
        if id_libro is None:
            print("Libro no encontrado")
        if id_prestamo is None:
            print("Prestamo no encontrado")

        query = Prestamos_librosModel.insert().values(id_libro=id_libro, id_prestamo=id_prestamo)
        try:
            db.session.execute(query)
            db.session.commit()
        except:
            return 'Formato no correcto', 400
        return 'Creado con exito', 201