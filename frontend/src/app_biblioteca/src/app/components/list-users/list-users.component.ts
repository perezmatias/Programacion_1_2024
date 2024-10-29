import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { UsuarioService } from '../../services/usuario.service';

@Component({
  selector: 'app-list-users',
  templateUrl: './list-users.component.html',
  styleUrl: './list-users.component.css'
})
export class ListUsersComponent {
  searchQuery = '';
  // arrayUsuarios = [
  //   {
  //     id: 1,
  //     nombre: 'Carlos'
  //   },
  //   {
  //     id: 2,
  //     nombre: 'Juan'
  //   },
  //   {
  //     id: 3,
  //     nombre: 'Pedro'
  //   },
  //   {
  //     id: 4,
  //     nombre: 'Usuario 4'
  //   }
  // ]

  arrayUsuarios:any[] = []

  filteredUsers:any[] = []

  constructor(
    private router: Router,
    private usuarioService: UsuarioService
  ){
  } 

  ngOnInit() {
    this.usuarioService.getUsers().subscribe((rta:any) => {
      console.log('usuarios api: ',rta);
      this.arrayUsuarios = rta.usuarios || [];
      this.filteredUsers = [...this.arrayUsuarios]
    })
  }

  editarusuario(user: any) {
    console.log('Estoy editando', user);
    this.router.navigate(['/editusers/' + user.id + '/Editar']);
  }

  buscar(query: string) {
    this.filteredUsers = this.arrayUsuarios.filter(user => user.nombre.toLowerCase().includes(query.toLowerCase()));
  }
}
