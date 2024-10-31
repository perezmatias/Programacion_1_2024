import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { PrestamoService } from '../../services/prestamo.service';

@Component({
  selector: 'app-list-loans',
  templateUrl: './list-loans.component.html',
  styleUrl: './list-loans.component.css'
})
export class ListLoansComponent {
  searchQuery = '';

  idFilter = '';

  arrayPrestamos: any[] = [];

  filteredLoans:any [] = [];

  total: number = 0; // Total de usuarios
  pages: number = 0; // Total de páginas
  currentPage: number = 1; // Página actual

  constructor(
    private router: Router,
    private prestamoService: PrestamoService
  ){
  }

  ngOnInit() {
    this.loadPrestamos();
  }

  loadPrestamos(page: number = 1) {
    this.prestamoService.getPrestamos(page, 10).subscribe((rta: any) => {
      console.log('prestamos api: ', rta);
      this.arrayPrestamos = rta.prestamos || [];
      this.filteredLoans = [...this.arrayPrestamos];
      this.total = rta.total;
      this.pages = rta.pages;
      this.currentPage = page; // Actualizar la página actual
    });
  }

  aplicarFiltros() {
    this.filteredLoans = this.arrayPrestamos.filter(prestamo => {
      const matchesFR = prestamo.Fecha_retiro.toLowerCase().includes(this.searchQuery.toLowerCase());
      const matchesFD = prestamo.Fecha_devolucion.toLowerCase().includes(this.searchQuery.toLowerCase());
      const matchesId = prestamo.id.toLowerCase().includes(this.idFilter.toLowerCase());

      // Retorna verdadero si coincide con nombre, apellido o rol
      return (matchesFR || matchesFD) && matchesId;
    });
  }
  
  editarprestamo(loan: any) {
    console.log('Estoy editando', loan);
    this.router.navigate(['/editprestamos/' + loan.id + '/Editar']);
  }

  deletePrestamo(id: string) {
    if (confirm('¿Estás seguro de que deseas eliminar este prestamo?')) {
      this.prestamoService.deletePrestamos(id).subscribe(response => {
        console.log('Prestamo eliminado', response);
        this.arrayPrestamos = this.arrayPrestamos.filter(prestamo => prestamo.id !== id); // Filtrar el usuario eliminado
        this.filteredLoans = [...this.arrayPrestamos]; // Actualizar la lista de usuarios filtrados
      });
    }
  }

  buscar(query: string) {
    this.searchQuery = query; // Actualiza la consulta de búsqueda
    this.aplicarFiltros(); // Aplica los filtros después de actualizar la búsqueda
  }

  cambiarId(nuevoId: string) {
    this.idFilter = nuevoId; // Actualiza el filtro de rol
    this.aplicarFiltros(); // Aplica los filtros después de actualizar
  }

  nextPage() {
    if (this.currentPage < this.pages) {
      this.loadPrestamos(this.currentPage + 1);
    }
  }

  previousPage() {
    if (this.currentPage > 1) {
      this.loadPrestamos(this.currentPage - 1);
    }
  }
}