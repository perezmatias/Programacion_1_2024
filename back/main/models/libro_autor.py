from .. import db 

class Libro_Autor(db.Model):
    id_libro = db.Colum(db.Integer)
    id_autor = db.Colum(db.Integer)
    
    #Convertir objeto en JSON
    def to_json(self):
        Libro_Autor_json = {
            'id_libro': self.id_libro,
            'id_autor': self.id_autor,

        }
        return Libro_Autor_json