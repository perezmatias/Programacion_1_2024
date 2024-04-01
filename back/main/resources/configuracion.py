from flask_restful import Resource
from flask import request

CONFIGURACION={
    1: {
        'nombre': 'Inserte nombre',
        'apertura': '12:00',
        'cierre': '18:00'
    }
}

class Configuracion(Resource):
    def get(self):
        return CONFIGURACION
    
    def put(self):
            data = request.get_json()
            if CONFIGURACION:
                CONFIGURACION[1].update(data)
                return CONFIGURACION[1], 201
            else:
                 return {'message': 'No hay configuración existente'}, 404