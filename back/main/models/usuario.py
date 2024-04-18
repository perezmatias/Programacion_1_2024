from .. import db 

class Usuario(db.Model):
    id = db.Colum(db.Integer, primary_key=True)
    nombre = db.Colum(db.String(100), nullable = False)
    apellido = db.Colum(db.String(100), nullable = False)
    telefono = db.Colum(db.Integer)
    contraseña = db.Colum(db.String(100), nullable = False)
    rol = db.Colum(db.String(100), nullable = False)
    
    #Convertir objeto en JSON
    def to_json(self):
        Usuario_json = {
            'id': self.id,
            'nombre': str(self.nombre),
            'apellido': str(self.apellido),
            'telefono': self.telefono,
            'contraseña': str(self.contraseña),
            'rol': str(self.rol),

        }
        return Usuario_json