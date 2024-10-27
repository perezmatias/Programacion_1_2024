import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './pages/login/login.component';
import { RegisterComponent } from './pages/register/register.component';
import { AdminComponent } from './pages/admin/admin.component';
import { ConfiguracionComponent } from './pages/configuracion/configuracion.component';
import { UsuariosComponent } from './pages/usuarios/usuarios.component';
import { LibrosComponent } from './pages/libros/libros.component';
import { EditlibrosComponent } from './pages/editlibros/editlibros.component';
import { PrestamosComponent } from './pages/prestamos/prestamos.component';
import { EditprestamosComponent } from './pages/editprestamos/editprestamos.component';
import { LibrosuserComponent } from './pages/librosuser/librosuser.component';
import { NotificacionesComponent } from './pages/notificaciones/notificaciones.component';
import { UsuarioComponent } from './pages/usuario/usuario.component';
import { authsessionGuard } from './guards/authsession.guard';
import { EditusersComponent } from './pages/editusers/editusers.component';
const routes: Routes = [

  { path:'login', component:LoginComponent },
  { path:'register', component:RegisterComponent},
  { path:'admin', component:AdminComponent},
  { path:'configuracion', component:ConfiguracionComponent, canActivate:[authsessionGuard]},
  { path:'usuarios', component:UsuariosComponent, canActivate:[authsessionGuard]},
  { path:'libros', component:LibrosComponent, canActivate:[authsessionGuard]},
  { path:'editlibros/:id/:tipo_op', component:EditlibrosComponent},
  { path:'prestamos', component:PrestamosComponent, canActivate:[authsessionGuard]},
  { path:'editprestamos', component:EditprestamosComponent},
  { path:'usuario', component:UsuarioComponent},
  { path:'librosuser', component:LibrosuserComponent},
  { path:'notificaciones', component:NotificacionesComponent},
  { path:'editusers/:id/:tipo_op', component:EditusersComponent},

  { path: '', redirectTo: '/login', pathMatch:'full'}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
