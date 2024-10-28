import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './pages/login/login.component';
import { RegisterComponent } from './pages/register/register.component';
import { AdminComponent } from './pages/admin/admin.component';
import { NavComponent } from './components/nav/nav.component';
import { UsuariosComponent } from './pages/usuarios/usuarios.component';
import { SearchComponent } from './components/search/search.component';
import { LibrosComponent } from './pages/libros/libros.component';
import { EditlibrosComponent } from './pages/editlibros/editlibros.component';
import { PrestamosComponent } from './pages/prestamos/prestamos.component';
import { EditprestamosComponent } from './pages/editprestamos/editprestamos.component';
import { UsuarioComponent } from './pages/usuario/usuario.component';
import { LibrosuserComponent } from './pages/librosuser/librosuser.component';
import { NotificacionesComponent } from './pages/notificaciones/notificaciones.component';
import { HttpClient, HttpClientModule} from '@angular/common/http';
import { FormsModule, ReactiveFormsModule} from '@angular/forms';
import { ListUsersComponent } from './components/list-users/list-users.component';
import { AbmComponent } from './components/abm/abm.component';
import { ListBooksComponent } from './components/list-books/list-books.component';
import { ListLoansComponent } from './components/list-loans/list-loans.component';
import { EditusersComponent } from './pages/editusers/editusers.component';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    RegisterComponent,
    AdminComponent,
    NavComponent,
    UsuariosComponent,
    SearchComponent,
    LibrosComponent,
    EditlibrosComponent,
    PrestamosComponent,
    EditprestamosComponent,
    UsuarioComponent,
    LibrosuserComponent,
    NotificacionesComponent,
    ListUsersComponent,
    AbmComponent,
    ListBooksComponent,
    ListLoansComponent,
    EditusersComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    ReactiveFormsModule,
    FormsModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
