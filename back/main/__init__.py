from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
import main.resources as resources

api = Api()

def create_app():
    app= Flask(__name__)
    load_dotenv()
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
    api.add_resource(resources.ConfiguracionResources, "/configuracion")
    api.add_resource(resources.ComentarioReources, "/comentario/<id>")
    api.add_resource(resources.ValoracionesResources, "/valoraciones")
    api.add_resource(resources.ComentariosResources, "/comentarios")
    api.init_app(app)

    return app