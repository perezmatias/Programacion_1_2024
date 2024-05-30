from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import UsuarioModel, PrestamoModel
from sqlalchemy import func, desc
from flask_jwt_extended import jwt_required, get_jwt_identity
from main.auth.decorators import role_required

class Usuario(Resource):
    @jwt_required(optional=True)
    def get(self, id):
        usuario = db.session.query(UsuarioModel).get_or_404(id)
        current_identity = get_jwt_identity()
        if current_identity:
            return usuario.to_json_complete()
        else:
            return usuario.to_json()
    
    @role_required(roles = ["admin", "bibliotecario"])
    def delete(self, id):
        usuario = db.session.query(UsuarioModel).get_or_404(id)
        db.session.delete(usuario)
        db.session.commit()
        return usuario.to_json(), 204
    
    @jwt_required()
    def put(self, id):
        usuario = db.session.query(UsuarioModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(usuario, key, value)
        db.session.add(usuario)
        db.session.commit()
        return usuario.to_json() , 201


class Usuarios(Resource):
    @role_required(roles = ["admin"])
    def get(self):
        page = 1
        per_page = 10
        usuarios = db.session.query(UsuarioModel)
        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))

        #FILTROS
        if request.args.get('nroPrestamos'):
            usuarios=usuarios.outerjoin(UsuarioModel.prestamos).group_by(UsuarioModel.id).having(func.count(PrestamoModel.id) >= int(request.arg.get('nroPrestamos')))
        
        if request.args.get('nombre'):
            usuarios=usuarios.filter(UsuarioModel.nombre.like("%"+request.args.get('nombre')+"%"))
        
        if request.args.get('sortby_nombre'):
            usuarios=usuarios.order_by(desc(UsuarioModel.nombre))
        
        if request.args.get('apellido'):
            usuarios=usuarios.filter(UsuarioModel.apellido.like("%"+request.args.get('apellido')+"%"))
        
        if request.args.get('sortby_apellido'):
            usuarios=usuarios.order_by(desc(UsuarioModel.apellido))
        
        if request.args.get('sortby_nroPrestamos'):
            usuarios=usuarios.outerjoin(UsuarioModel.prestamos).group_by(UsuarioModel.id).order_by(func.count(PrestamoModel.id).desc())
        
        usuarios = usuarios.paginate(page=page,per_page=per_page, error_out=True)

        return jsonify({'usuarios': [usuario.to_json() for usuario in usuarios],
                    'total': usuarios.total,
                    'pages': usuarios.pages,
                    'page': page
                })

    def post(self):
        usuario = UsuarioModel.from_json(request.get_json())
        db.session.add(usuario)
        db.session.commit()
        return usuario.to_json(), 201
    