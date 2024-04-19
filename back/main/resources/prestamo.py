from flask_restful import Resource
from flask import request, jsonify
from .. import db
from main.models import PrestamoModel
from datetime import datetime

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
        prestamos = db.session.query(PrestamoModel).all()
        return jsonify([prestamo.to_json() for prestamo in prestamos])
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