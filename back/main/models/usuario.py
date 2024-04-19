from .. import db 

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable = False)
    apellido = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100),nullable = False)
    telefono = db.Column(db.Integer)
    contraseña = db.Column(db.String(100), nullable = False)
    rol = db.Column(db.String(100), nullable = False)
    
    #Convertir objeto en JSON
    def to_json(self):
        Usuario_json = {
            'id': self.id,
            'nombre': str(self.nombre),
            'apellido': str(self.apellido),
            'email': str(self.email),
            'telefono': str(self.telefono),
            'contraseña': str(self.contraseña),
            'rol': str(self.rol),

        }
        return Usuario_json