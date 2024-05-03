from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import PrestamoModel, UsuarioModel
from datetime import datetime
from sqlalchemy import func, desc

#PRESTAMOS = {
#    1: {
#        'id_libro': '1',
#        'id_usuario': '1',
#        'fecha_prestamo': '2021-10-01',
#        'fecha_devolucion': '2021-10-15'
#    },
#    2: {
#        'id_libro': '2',
#        'id_usuario': '2',
#        'fecha_prestamo': '2021-10-01',
#        'fecha_devolucion': '2021-10-15'
#    },
#    3: {
#        'id_libro': '3',
#        'id_usuario': '3',
#        'fecha_prestamo': '2021-10-01',
#        'fecha_devolucion': '2021-10-15'
#    }
#}


class Prestamo(Resource):
    def get(self, id):
        prestamo = db.session.query(PrestamoModel).get_or_404(id)
        return prestamo.to_json()
    #    if int(id) in PRESTAMOS:
    #        return PRESTAMOS[int(id)]
    #    return 'No existe el id', 404
    
    def delete(self, id):
        prestamo = db.session.query(PrestamoModel).get_or_404(id)
        db.session.delete(prestamo)
        db.session.commit()
        return prestamo.to_json(), 204
    #    if int(id) in PRESTAMOS:
    #        del PRESTAMOS[int(id)]
    #        return '', 204
    #    return 'No existe el id', 404
    
    def put(self, id):
        prestamo = db.session.query(PrestamoModel).get_or_404(id)
        data = request.get_json()
        for key, value in data.items():
            if key in ['Fecha_retiro', 'Fecha_devolucion']:
                setattr(prestamo, key, datetime.strptime(value, '%d-%m-%Y'))
            else:
                setattr(prestamo, key, value)
        db.session.commit()
        return prestamo.to_json() , 201
    #    if int(id) in PRESTAMOS:
    #        Prestamo=PRESTAMOS[int(id)]
    #        data = request.get_json()
    #        Prestamo.update(data)
    #        return "", 201
    #    return "No existe el id", 404

class Prestamos(Resource):
    def get(self):
        page = 1
        per_page = 10
        prestamos = db.session.query(PrestamoModel)
        if request.args.get('page'):
            page = int(request.args.get('page'))
        if request.args.get('per_page'):
            per_page = int(request.args.get('per_page'))

        # Filtrado por id
        if request.args.get('id'):
            prestamos=prestamos.filter(PrestamoModel.id.like("%"+request.args.get('id')+"%"))
        
        if request.args.get('sortby_id'):
            prestamos=prestamos.order_by(desc(PrestamoModel.id))

        #Filtrado por fecha_retiro
        if request.args.get('FechaRet'):
            fecha_retiro_str = request.args.get('FechaRet')
            try:
                fecha_retiro = datetime.strptime(fecha_retiro_str, '%d-%m-%Y')
            except ValueError:
                    fecha_retiro = datetime.strptime(fecha_retiro_str, '%Y-%m-%d')
            
            fecha_retiro_str = fecha_retiro.strftime('%Y-%m-%d')
            prestamos = prestamos.filter(PrestamoModel.Fecha_retiro.like("%"+ fecha_retiro_str +"%"))
        
        if request.args.get('FechaRet'):
            prestamos=prestamos.order_by(desc(PrestamoModel.Fecha_retiro))

        #Filtrado por fecha_devolucion
        if request.args.get('FechaDev'):
            fecha_devolucion_str = request.args.get('FechaDev')
            try:
                fecha_devolucion = datetime.strptime(fecha_devolucion_str, '%d-%m-%Y')
            except ValueError:
                    fecha_devolucion = datetime.strptime(fecha_devolucion_str, '%Y-%m-%d')
            
            fecha_devolucion_str = fecha_devolucion.strftime('%Y-%m-%d')
            prestamos = prestamos.filter(PrestamoModel.Fecha_devolucion.like("%"+ fecha_devolucion_str +"%"))
        
        if request.args.get('FechaDev'):
            prestamos=prestamos.order_by(desc(PrestamoModel.Fecha_devolucion))

        #Filtrado respecto del Usuario
        if request.args.get('user_id'):
            user_id = request.args.get('user_id')
            prestamos = prestamos.filter(PrestamoModel.id_usuario == user_id)
        
        if request.args.get('nombre'):
            nombre = request.args.get('nombre')
            prestamos = prestamos.join(UsuarioModel).filter(UsuarioModel.nombre.like("%" + nombre + "%"))

        if request.args.get('apellido'):
            apellido = request.args.get('apellido')
            prestamos = prestamos.join(UsuarioModel).filter(UsuarioModel.apellido.like("%" + apellido + "%"))
        
        
        prestamos = prestamos.paginate(page=page, per_page=per_page, error_out=True)

        return jsonify({'prestamos': [prestamo.to_json() for prestamo in prestamos],
                        'total': prestamos.total,
                        'pages': prestamos.pages,
                        'page': page
                    })


        #prestamos = db.session.query(PrestamoModel).all()
        #return jsonify([prestamo.to_json() for prestamo in prestamos])
    #    return PRESTAMOS
    
    def post(self):
        prestamo = PrestamoModel.from_json(request.get_json())
        db.session.add(prestamo)
        db.session.commit()
        return prestamo.to_json(), 201

    #    Prestamo = request.get_json()
    #    id = int(max(PRESTAMOS.keys())) + 1
    #    PRESTAMOS[id] = Prestamo
    #    return PRESTAMOS[id], 201