from .. import db 

class Reseña(db.Model):
    id = db.Colum(db.Integer, primary_key=True)
    id_usuario = db.Colum(db.Integer)
    id_libro = db.Colum(db.Integer)
    comentario = db.Colum(db.String(100), nullable = False)
    valoracion = db.Colum(db.Integer)

    
    #Convertir objeto en JSON
    def to_json(self):
        Reseña_json = {
            'id': self.id,
            'id_usuario': self.id_usuario,
            'id_libro': self.id_libro,
            'comentario': str(self.comentario),
            'valoracion': self.valoracion,
        }
        return Reseña_json