from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api
import main.resources as resources



def create_app():
    app= Flask(__name__)
    load_dotenv()
    Api.add_resource(resources.librosresources, "/libros")
    Api.add_resource(resources.libroresources, "/libro/<id>")
    Api.add_resource(resources.prestamosresources, "/prestamos")
    Api.add_resource(resources.prestamoresources, "/prestamo/<id>")
    Api.add_resource(resources.usuariosresources, "/usuarios")
    Api.add_resource(resources.usuarioresources, "/usuario/<id>")
    Api.add_resource(resources.valoracionresources, "/valoracion/<id>")
    Api.add_resource(resources.notificacionresources, "/notificacion")
    Api.add_resource(resources.loginresources, "/login")
    Api.add_resource(resources.signinresources, "/signin")
    Api.add_resource(resources.configuracionresources, "/configuracion")
    Api.add_resource(resources.comentarioreources, "/comentario/<id>")
    

    return app