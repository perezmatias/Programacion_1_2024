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

  rolFilter = '';

  arrayUsuarios:any[] = [];

  filteredUsers:any[] = [];

  total: number = 0; // Total de usuarios
  pages: number = 0; // Total de páginas
  currentPage: number = 1; // Página actual

  constructor(
    private router: Router,
    private usuarioService: UsuarioService
  ){
  } 

  ngOnInit() {
    this.loadUsers();
  }

  loadUsers(page: number = 1) {
    this.usuarioService.getUsers(page, 10).subscribe((rta: any) => {
      console.log('usuarios api: ', rta);
      this.arrayUsuarios = rta.usuarios || [];
      this.filteredUsers = [...this.arrayUsuarios];
      this.total = rta.total;
      this.pages = rta.pages;
      this.currentPage = page; // Actualizar la página actual
    });
  }

  aplicarFiltros() {
    this.filteredUsers = this.arrayUsuarios.filter(user => {
      const matchesNombre = user.nombre.toLowerCase().includes(this.searchQuery.toLowerCase());
      const matchesApellido = user.apellido.toLowerCase().includes(this.searchQuery.toLowerCase());
      const matchesRol = user.rol.toLowerCase().includes(this.rolFilter.toLowerCase());

      // Retorna verdadero si coincide con nombre, apellido o rol
      return (matchesNombre || matchesApellido) && matchesRol;
    });
  }

  editarusuario(user: any) {
    console.log('Estoy editando', user);
    this.router.navigate(['/editusers/' + user.id + '/Editar']);
  }

  deleteUser(id: string) {
    if (confirm('¿Estás seguro de que deseas eliminar este usuario?')) {
      this.usuarioService.deleteUser(id).subscribe(response => {
        console.log('Usuario eliminado', response);
        this.arrayUsuarios = this.arrayUsuarios.filter(user => user.id !== id); // Filtrar el usuario eliminado
        this.filteredUsers = [...this.arrayUsuarios]; // Actualizar la lista de usuarios filtrados
      });
    }
  }

  buscar(query: string) {
    this.searchQuery = query; // Actualiza la consulta de búsqueda
    this.aplicarFiltros(); // Aplica los filtros después de actualizar la búsqueda
  }

  cambiarRol(nuevoRol: string) {
    this.rolFilter = nuevoRol; // Actualiza el filtro de rol
    this.aplicarFiltros(); // Aplica los filtros después de actualizar el rol
  }

  nextPage() {
    if (this.currentPage < this.pages) {
      this.loadUsers(this.currentPage + 1);
    }
  }

  previousPage() {
    if (this.currentPage > 1) {
      this.loadUsers(this.currentPage - 1);
    }
  }
}
