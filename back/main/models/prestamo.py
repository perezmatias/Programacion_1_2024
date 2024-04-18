from .. import db 

class Prestamo(db.Model):
    id_prestamo = db.Colum(db.Integer, primary_key=True)
    id_usuario = db.Colum(db.Integer)
    id_libro = db.Colum(db.Integer)
    Fecha_retiro = db.Colum(db.date, nullable = False)
    Fecha_devolucion = db.Colum(db.date, nullable = False)
    
    #Convertir objeto en JSON
    def to_json(self):
        Prestamo_json = {
            'id_prestamo': self.id_prestamo,
            'id_usuario': self.id_usuario,
            'id_libro': self.id_libro,
            'fecha_retiro': ,
            'fecha_devolucion':,

        }
        return Prestamo_json