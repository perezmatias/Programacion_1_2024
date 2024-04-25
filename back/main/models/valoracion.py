from .. import db 

class Valoracion(db.Model):
    __tablename__ = 'valoraciones'
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer)
    id_libro = db.Column(db.Integer)
    comentario = db.Column(db.String(100), nullable = False)
    valoracion = db.Column(db.Integer)

    def __repr__(self):
        return '<Valoracion: {}>'.format(self.id)
    
    def to_json(self):
        valoracion_json = {
            'id': self.id,
            'id_usuario': self.id_usuario,
            'id_libro': self.id_libro,
            'comentario': self.comentario,
            'valoracion': self.valoracion
        }
        return valoracion_json

    def to_json_short(self):
        return self.to_json()

    @staticmethod
    def from_json(valoracion_json):
        id = valoracion_json.get('id')
        id_usuario = valoracion_json.get('id_usuario')
        id_libro = valoracion_json.get('id_libro')
        comentario = valoracion_json.get('comentario')
        valoracion = valoracion_json.get('valoracion')
        return Valoracion(id=id, id_usuario=id_usuario, id_libro=id_libro,
                          comentario=comentario, valoracion=valoracion)