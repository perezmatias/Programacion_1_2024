from .. import db 

class Libro(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable = False)
    genero = db.Column(db.String(100), nullable = False)
    autor = db.Column(db.String(100), nullable = False)
    cant_ejemplares = db.Column(db.Integer)
    
    #Convertir objeto en JSON
    def to_json(self):
        Libro_json = {
            'id': self.id,
            'genero': str(self.genero),
            'nombre': str(self.nombre),
            'autor': str(self.autor),
            'cant_ejemplares': str(self.cant_ejemplares),

        }
        return Libro_json