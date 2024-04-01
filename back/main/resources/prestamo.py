from flask_restful import Resource
from flask import request

PRESTAMOS = {
    1: {
        'id_libro': '1',
        'id_usuario': '1',
        'fecha_prestamo': '2021-10-01',
        'fecha_devolucion': '2021-10-15'
    },
    2: {
        'id_libro': '2',
        'id_usuario': '2',
        'fecha_prestamo': '2021-10-01',
        'fecha_devolucion': '2021-10-15'
    },
    3: {
        'id_libro': '3',
        'id_usuario': '3',
        'fecha_prestamo': '2021-10-01',
        'fecha_devolucion': '2021-10-15'
    }
}


class Prestamo(Resource):
    def get(self, id):
        if int(id) in PRESTAMOS:
            return PRESTAMOS[int(id)]
        return 'No existe el id', 404
    
    def delete(self, id):
        if int(id) in PRESTAMOS:
            del PRESTAMOS[int(id)]
            return '', 204
        return 'No existe el id', 404
    
    def put(self, id):
        if int(id) in PRESTAMOS:
            Prestamo=PRESTAMOS[int(id)]
            data = request.get_json()
            Prestamo.update(data)
            return "", 201
        return "No existe el id", 404

class Prestamos(Resource):
    def get(self):
        return PRESTAMOS
    
    def post(self):
        Prestamo = request.get_json()
        id = int(max(PRESTAMOS.keys())) + 1
        PRESTAMOS[id] = Prestamo
        return PRESTAMOS[id], 201