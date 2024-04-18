from .. import db 

class Prestamo_Libro(db.Model):
    id_libro = db.Colum(db.Integer)
    id_prestamo = db.Colum(db.Integer)
    
    #Convertir objeto en JSON
    def to_json(self):
        Prestamo_Libro_json = {
            'id_libro': self.id_libro,
            'id_prestamo': self.id_prestamo,
        }
        return Prestamo_Libro_json