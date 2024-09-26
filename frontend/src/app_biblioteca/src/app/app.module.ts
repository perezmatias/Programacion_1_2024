import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './pages/login/login.component';
import { RegisterComponent } from './pages/register/register.component';
import { AdminComponent } from './pages/admin/admin.component';
import { NavComponent } from './components/nav/nav.component';
import { ConfiguracionComponent } from './pages/configuracion/configuracion.component';
import { UsuariosComponent } from './pages/usuarios/usuarios.component';
import { SearchComponent } from './components/search/search.component';
import { LibrosComponent } from './pages/libros/libros.component';
import { EditlibrosComponent } from './pages/editlibros/editlibros.component';
import { PrestamosComponent } from './pages/prestamos/prestamos.component';
import { EditprestamosComponent } from './pages/editprestamos/editprestamos.component';
import { UsuarioComponent } from './pages/usuario/usuario.component';
import { LibrosuserComponent } from './pages/librosuser/librosuser.component';
import { NotificacionesComponent } from './pages/notificaciones/notificaciones.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    RegisterComponent,
    AdminComponent,
    NavComponent,
    ConfiguracionComponent,
    UsuariosComponent,
    SearchComponent,
    LibrosComponent,
    EditlibrosComponent,
    PrestamosComponent,
    EditprestamosComponent,
    UsuarioComponent,
    LibrosuserComponent,
    NotificacionesComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
