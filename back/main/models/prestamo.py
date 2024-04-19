from .. import db 
from datetime import datetime

class Prestamo(db.Model):
    id_prestamo = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer)
    id_libro = db.Column(db.Integer)
    Fecha_retiro = db.Column(db.Date, nullable = False)
    Fecha_devolucion = db.Column(db.Date, nullable = False)
    
    #Convertir objeto en JSON
    def to_json(self):
        Prestamo_json = {
            'id_prestamo': self.id_prestamo,
            'id_usuario': self.id_usuario,
            'id_libro': self.id_libro,
            'fecha_retiro': self.Fecha_retiro.strftime('%Y-%m-%d'),
            'fecha_devolucion':self.Fecha_devolucion.strftime('%Y-%m-%d'),

        }
        return Prestamo_json