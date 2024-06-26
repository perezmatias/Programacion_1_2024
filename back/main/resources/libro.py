from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import LibroModel, Autores_librosModel, AutorModel
from sqlalchemy import func, desc
from flask_jwt_extended import jwt_required, get_jwt_identity
from main.auth.decorators import role_required

class Libro(Resource):
    def get(self, id):
        libro = db.session.query(LibroModel).get_or_404(id)
        return libro.to_json_complete()

    @role_required(roles = ["admin", "bibliotecario"])
    def delete(self, id):
        libro = db.session.query(LibroModel).get_or_404(id)
        db.session.delete(libro)
        db.session.commit()
        return libro.to_json(), 204

    @role_required(roles = ["admin", "bibliotecario"])
    def put(self, id):
        libro = db.session.query(LibroModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(libro, key, value)
        db.session.add(libro)
        db.session.commit()
        return libro.to_json() , 201

class Libros(Resource):
    def get(self):
        page = 1
        per_page = 10
        libros = db.session.query(LibroModel)
        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))
        
        #FILTROS

        if request.args.get('nombre'):
            libros=libros.filter(LibroModel.nombre.like("%"+request.args.get('nombre')+"%"))

        if request.args.get('sortby_nombre'):
            libros=libros.order_by(desc(LibroModel.nombre))

        if request.args.get('genero'):
            libros=libros.filter(LibroModel.genero.like("%"+request.args.get('genero')+"%"))

        if request.args.get('sortby_genero'):
            libros=libros.order_by(desc(LibroModel.genero))

        if request.args.get('autor_id'):
            libros=libros.filter(LibroModel.autores.any(id=request.args.get('autor_id')))

        if request.args.get('autor_name'):
            autor_name= request.args.get('autor_name')
            libros = libros.filter(LibroModel.autores.any(AutorModel.nombre.like("%" + autor_name + "%")))
        
        if request.args.get('autor_apellido'):
            autor_apellido= request.args.get('autor_apellido')
            libros = libros.filter(LibroModel.autores.any(AutorModel.apellido.like("%" + autor_apellido + "%")))



        libros=libros.paginate(page=page, per_page=per_page, error_out=True)
        return jsonify({'libros': [libro.to_json() for libro in libros],
                        'total': libros.total,
                        'pages': libros.pages,
                        'page': page
                    })

    @role_required(roles = ["admin", "bibliotecario"])
    def post(self):
        libro = LibroModel.from_json(request.get_json())
        db.session.add(libro)
        db.session.commit()
        return libro.to_json(), 201
