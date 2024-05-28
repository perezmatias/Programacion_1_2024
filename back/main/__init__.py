from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import os
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

api = Api()

db = SQLAlchemy()

migrate = Migrate()

jwt = JWTManager()

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
    migrate.init_app(app,db)

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
    api.add_resource(resources.Autores_librosResources, "/autolibro")
    api.add_resource(resources.Prestamos_librosResources, "/preslibro")
    api.init_app(app)

    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES'))
    jwt.init_app(app)

    from main.auth import routes
    app.register_blueprint(routes.auth)

    return app