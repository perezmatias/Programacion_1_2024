from .. import db 

class Libro(db.Model):
    id = db.Colum(db.Integer, primary_key=True)
    nombre = db.Colum(db.String(100), nullable = False)
    genero = db.Colum(db.String(100), nullable = False)
    autor = db.Colum(db.String(100), nullable = False)
    cant_ejemplares = db.Colum(db.Integer)
    
    #Convertir objeto en JSON
    def to_json(self):
        Libro_json = {
            'id': self.id,
            'genero': str(self.genero),
            'nombre': str(self.nombre),
            'autor': str(self.autor),
            'cant_ejemplares': self.cant_ejemplares,

        }
        return Libro_json