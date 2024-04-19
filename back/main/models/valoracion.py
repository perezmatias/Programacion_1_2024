from .. import db 

class Valoracion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer)
    id_libro = db.Column(db.Integer)
    comentario = db.Column(db.String(100), nullable = False)
    valoracion = db.Column(db.Integer)

    
    #Convertir objeto en JSON
    def to_json(self):
        Valoracion_json = {
            'id': self.id,
            'id_usuario': self.id_usuario,
            'id_libro': self.id_libro,
            'comentario': str(self.comentario),
            'valoracion': str(self.valoracion),
        }
        return Valoracion_json