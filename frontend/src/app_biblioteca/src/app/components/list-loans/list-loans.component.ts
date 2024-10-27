import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-list-loans',
  templateUrl: './list-loans.component.html',
  styleUrl: './list-loans.component.css'
})
export class ListLoansComponent {
  searchQuery = '';
  arrayUsuarios = [
    {
      id: 1,
      nombre: 'Carlos'
    },
    {
      id: 2,
      nombre: 'Juan'
    },
    {
      id: 3,
      nombre: 'Pedro'
    },
    {
      id: 4,
      nombre: 'Usuario 4'
    }
  ]
  filteredUsers = [...this.arrayUsuarios]
  constructor(
    private router: Router
  ){
  } 
  editarusuario(user:any) {
    console.log('Estoy editando', user);
    this.router.navigate(['/usuario/'+user.id+'/Editar']);
  }
  buscar() {
    console.log('buscar: ', this.searchQuery);
    this.filteredUsers = this.arrayUsuarios.filter(user => user.nombre.includes(this.searchQuery));
  }
}
