from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import os

api = Api()

db = SQLAlchemy()

def create_app():
    app= Flask(__name__)
    
    load_dotenv()

#Si no existe el archivo de base de datos crearlo (solo válido si se utiliza SQLite)
    if not os.path.exists(os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME')):
        os.mknod(os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME'))    
        
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#Url de configuración de base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////'+os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME')
    db.init_app(app)

    import main.resources as resources
    api.add_resource(resources.LibrosResources, "/libros")
    api.add_resource(resources.LibroResources, "/libro/<id>")
    api.add_resource(resources.PrestamosResources, "/prestamos")
    api.add_resource(resources.PrestamoResources, "/prestamo/<id>")
    api.add_resource(resources.UsuariosResources, "/usuarios")
    api.add_resource(resources.UsuarioResources, "/usuario/<id>")
    api.add_resource(resources.ValoracionResources, "/valoracion/<id>")
    api.add_resource(resources.NotificacionResources, "/notificacion")
    api.add_resource(resources.LoginResources, "/login")
    api.add_resource(resources.SigninResources, "/signin")
    api.add_resource(resources.ValoracionesResources, "/valoraciones")
    api.add_resource(resources.AutorResources, "/autor/<id>")
    api.add_resource(resources.AutoresResources, "/autores")
    api.init_app(app)

    return app