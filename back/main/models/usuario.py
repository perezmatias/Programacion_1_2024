from .. import db 
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable = False)
    apellido = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100),unique=True, index=True, nullable = False)
    telefono = db.Column(db.Integer)
    contraseña = db.Column(db.String(100), nullable = False)
    rol = db.Column(db.String(100), nullable = False, server_default="users")

    notificaciones = db.relationship("Notificacion", back_populates="usuarios",cascade="all, delete-orphan")
    valoraciones = db.relationship("Valoracion", back_populates="usuarios",cascade="all, delete-orphan")
    prestamos = db.relationship("Prestamo", back_populates="usuarios",cascade="all, delete-orphan")

    @property
    def plain_password(self):
        raise AttributeError('Password cant be read')
    
    @plain_password.setter
    def plain_password(self, contraseña):
        self.contraseña = generate_password_hash(contraseña)
    #Método que compara una contraseña en texto plano con el hash guardado en la db
    def validate_pass(self,contraseña):
        return check_password_hash(self.contraseña, contraseña)

    def __repr__(self):
        return '<Usuario: {} {}>'.format(self.nombre, self.apellido)
    
    def to_json(self):
        usuario_json = {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'email': self.email,
            'telefono': self.telefono,
            'contraseña': self.contraseña,
            'rol': self.rol
        }
        return usuario_json
    
    def to_json_complete(self):
        prestamos = [prestamo.to_json() for prestamo in self.prestamos]
        prestamo_json = {
            'id': self.id,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'email': self.email,
            'telefono': self.telefono,
            'contraseña': self.contraseña,
            'rol': self.rol,
            'prestamos':prestamos

        }
        return prestamo_json

    def to_json_short(self):
        return self.to_json()

    @staticmethod
    def from_json(usuario_json):
        id = usuario_json.get('id')
        nombre = usuario_json.get('nombre')
        apellido = usuario_json.get('apellido')
        email = usuario_json.get('email')
        telefono = usuario_json.get('telefono')
        contraseña = usuario_json.get('contraseña')
        rol = usuario_json.get('rol')
        return Usuario(id=id, nombre=nombre, apellido=apellido, email=email,
                        telefono=telefono, plain_password=contraseña ,rol=rol)