from .. import db 

class Libro(db.Model):
    __tablename__ = 'libros'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable = False)
    genero = db.Column(db.String(100), nullable = False)
    cant_ejemplares = db.Column(db.Integer)

    valoraciones = db.relationship("Valoracion", back_populates="libros",cascade="all, delete-orphan")
    
    def __repr__(self):
        return '<Libro: {}>'.format(self.nombre)
    
    def to_json(self):
        libro_json = {
            'id': self.id,
            'nombre': self.nombre,
            'genero': self.genero,
            'cant_ejemplares': self.cant_ejemplares
        }
        return libro_json
    
    def to_json_complete(self):
        valoraciones = [valoracion.to_json() for valoracion in self.valoraciones]
        valoracion_json = {
            'id': self.id,
            'nombre': self.nombre,
            'genero': self.genero,
            'cant_ejemplares': self.cant_ejemplares,
            'valoraciones':valoraciones

        }
        return valoracion_json

    def to_json_short(self):
        return self.to_json()

    @staticmethod
    def from_json(libro_json):
        id = libro_json.get('id')
        nombre = libro_json.get('nombre')
        genero = libro_json.get('genero')
        autor = libro_json.get('autor')
        cant_ejemplares = libro_json.get('cant_ejemplares')
        return Libro(id=id, nombre=nombre, genero=genero, autor=autor, cant_ejemplares=cant_ejemplares)