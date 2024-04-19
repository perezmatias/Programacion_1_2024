from .. import db 

class Notificacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer)
    descripcion = db.Column(db.String(100), nullable = False)

    def __repr__(self):
        return '<Notificacion: {}>'.format(self.descripcion)
    
    def to_json(self):
        notificacion_json = {
            'id': self.id,
            'id_usuario': self.id_usuario,
            'descripcion': self.descripcion,
        }
        return notificacion_json

    def to_json_short(self):
        return self.to_json()

    @staticmethod
    def from_json(notificacion_json):
        id = notificacion_json.get('id')
        id_usuario = notificacion_json.get('id_usuario')
        descripcion = notificacion_json.get('descripcion')
        return Notificacion(id=id, id_usuario=id_usuario, descripcion=descripcion)