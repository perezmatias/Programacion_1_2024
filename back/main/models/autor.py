from .. import db 

class Autor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable = False)
    apellido = db.Column(db.String(100), nullable = False)
    
    #Convertir objeto en JSON
    def to_json(self):
        Autor_json = {
            'id': self.id,
            'nombre': str(self.nombre),
            'apellido': str(self.apellido),

        }
        return Autor_json