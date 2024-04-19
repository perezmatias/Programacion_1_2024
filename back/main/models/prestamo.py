from .. import db 
from datetime import datetime

class Prestamo(db.Model):
    id_prestamo = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer)
    id_libro = db.Column(db.Integer)
    Fecha_retiro = db.Column(db.Date, nullable = False)
    Fecha_devolucion = db.Column(db.Date, nullable = False)
    
    def __repr__(self):
        return '<Prestamo: {}>'.format(self.id_prestamo)
    
    def to_json(self):
        prestamo_json = {
            'id_prestamo': self.id_prestamo,
            'id_usuario': self.id_usuario,
            'id_libro': self.id_libro,
            'Fecha_retiro': str(self.Fecha_retiro),
            'Fecha_devolucion': str(self.Fecha_devolucion)
        }
        return prestamo_json

    def to_json_short(self):
        return self.to_json()

    @staticmethod
    def from_json(prestamo_json):
        id_prestamo = prestamo_json.get('id_prestamo')
        id_usuario = prestamo_json.get('id_usuario')
        id_libro = prestamo_json.get('id_libro')
        Fecha_retiro_str = prestamo_json.get('Fecha_retiro')
        Fecha_devolucion_str = prestamo_json.get('Fecha_devolucion')

        try:
            # Convertir las cadenas de texto en objetos de fecha de Python
            Fecha_retiro = datetime.strptime(Fecha_retiro_str, '%Y-%m-%d').date()
            Fecha_devolucion = datetime.strptime(Fecha_devolucion_str, '%Y-%m-%d').date()
        except ValueError:
            # Manejar el caso en que las fechas no estén en el formato correcto
            return None

        return Prestamo(id_prestamo=id_prestamo, id_usuario=id_usuario, id_libro=id_libro,
                        Fecha_retiro=Fecha_retiro, Fecha_devolucion=Fecha_devolucion)