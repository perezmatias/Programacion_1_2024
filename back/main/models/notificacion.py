from .. import db 

class Notificacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer)
    descripcion = db.Column(db.String(100), nullable = False)

    
    #Convertir objeto en JSON
    def to_json(self):
        Notificacion_json = {
            'id': self.id,
            'id_usuario': self.id_usuario,
            'descripcion': str(self.descripcion),

        }
        return Notificacion_json