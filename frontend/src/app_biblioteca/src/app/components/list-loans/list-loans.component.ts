import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-list-loans',
  templateUrl: './list-loans.component.html',
  styleUrl: './list-loans.component.css'
})
export class ListLoansComponent {
  searchQuery = '';
  arrayPrestamos = [
    {
      id: 1,
      nombre: 'Terror'
    },
    {
      id: 2,
      nombre: 'Accion'
    },
    {
      id: 3,
      nombre: 'Fantasia'
    },
    {
      id: 4,
      nombre: 'Misterio'
    }
  ]
  filteredLoans = [...this.arrayPrestamos]
  constructor(
    private router: Router
  ){
  } 
  editarprestamo(loan: any) {
    console.log('Estoy editando', loan);
    this.router.navigate(['/editprestamos/' + loan.id + '/Editar']);
  }

  buscar(query: string) {
    this.filteredLoans = this.arrayPrestamos.filter(loan => loan.nombre.toLowerCase().includes(query.toLowerCase()));
  }
}