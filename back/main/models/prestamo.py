from .. import db 
import json
from datetime import datetime

prestamos_libros = db.Table("prestamos_libros",
    db.Column("id_libro",db.Integer,db.ForeignKey("libros.id"),primary_key=True),
    db.Column("id_prestamo",db.Integer,db.ForeignKey("prestamos.id"),primary_key=True)
    )

class Prestamo(db.Model):
    __tablename__ = 'prestamos'
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey("usuarios.id"))
    Fecha_retiro = db.Column(db.DateTime, nullable = False)
    Fecha_devolucion = db.Column(db.DateTime, nullable = False)

    usuarios = db.relationship("Usuario", back_populates="prestamos", uselist=False, single_parent=True)

    libros = db.relationship('Libro', secondary=prestamos_libros, backref=db.backref('prestamos', lazy='dynamic'))
    
    def __repr__(self):
        return '<Prestamo: {}>'.format(self.id)
    
    def to_json(self):
        prestamo_json = {
            'id': self.id,
            'id_usuario': self.id_usuario,
            'Fecha_retiro': self.Fecha_retiro.strftime("%d-%m-%Y"),
            'Fecha_devolucion': self.Fecha_devolucion.strftime("%d-%m-%Y"),
            'libros' : [libro.to_json() for libro in self.libros]
        }
        return prestamo_json

    def to_json_short(self):
        return self.to_json()

    @staticmethod
    def from_json(prestamo_json):
        id = prestamo_json.get('id')
        id_usuario = prestamo_json.get('id_usuario')
        Fecha_retiro = datetime.strptime(prestamo_json.get('Fecha_retiro'), '%d-%m-%Y')
        Fecha_devolucion = datetime.strptime(prestamo_json.get('Fecha_devolucion'), '%d-%m-%Y')
        return Prestamo(id = id,
                        id_usuario = id_usuario,
                        Fecha_retiro = Fecha_retiro,
                        Fecha_devolucion = Fecha_devolucion)