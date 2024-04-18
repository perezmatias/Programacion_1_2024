from .. import db 

class Autor(db.Model):
    id = db.Colum(db.Integer, primary_key=True)
    nombre = db.Colum(db.String(100), nullable = False)
    apellido = db.Colum(db.String(100), nullable = False)
    
    #Convertir objeto en JSON
    def to_json(self):
        Autor_json = {
            'id': self.id,
            'nombre': str(self.nombre),
            'apellido': str(self.apellido),

        }
        return Autor_json