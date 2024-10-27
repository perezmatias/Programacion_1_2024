import { Component } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-list-books',
  templateUrl: './list-books.component.html',
  styleUrl: './list-books.component.css'
})
export class ListBooksComponent {
  searchQuery = '';
  arrayLibros = [
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
  filteredBooks = [...this.arrayLibros]
  constructor(
    private router: Router
  ){
  } 
  editarlibro(book: any) {
    console.log('Estoy editando', book);
    this.router.navigate(['/editlibros/' + book.id + '/Editar']);
  }

  buscar(query: string) {
    this.filteredBooks = this.arrayLibros.filter(book => book.nombre.toLowerCase().includes(query.toLowerCase()));
  }
}