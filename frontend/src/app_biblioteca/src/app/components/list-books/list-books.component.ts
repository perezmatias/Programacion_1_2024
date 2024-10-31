import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { LibroService } from '../../services/libro.service';

@Component({
  selector: 'app-list-books',
  templateUrl: './list-books.component.html',
  styleUrl: './list-books.component.css'
})
export class ListBooksComponent {
  searchQuery = '';
  autorFilter = '';
  arrayLibros:any[] = [];
  filteredBooks:any[] = [];

  total: number = 0; // Total de usuarios
  pages: number = 0; // Total de páginas
  currentPage: number = 1; // Página actual

  constructor(
    private router: Router,
    private libroService: LibroService
  ){
  } 

  ngOnInit() {
    this.loadLibros();
  }

  loadLibros(page: number = 1) {
    this.libroService.getLibros(page, 10).subscribe((rta: any) => {
      console.log('libros api): ',rta);
      this.arrayLibros = rta.libros || [];
      this.filteredBooks = [...this.arrayLibros];
      this.total = rta.total;
      this.pages = rta.pages;
      this.currentPage = page;
    });
  }

  aplicarFiltros() {
    this.filteredBooks = this.arrayLibros.filter(book => {
      const matchesNombre = book.nombre.toLowerCase().includes(this.searchQuery.toLocaleLowerCase());

      return (matchesNombre);
    });
  }

  editarlibro(book: any) {
    console.log('Estoy editando', book);
    this.router.navigate(['/editlibros/' + book.id + '/Editar']);
  }

  deleteLibro(id: string) {
    if (confirm('¿Estás seguro de que deseas eliminar este libro?')) {
      this.libroService.deleteLibro(id).subscribe(response =>{
        console.log('Libro eliminado', response);
        this.arrayLibros = this.arrayLibros.filter(book => book.id !== id);
        this.filteredBooks = [...this.arrayLibros];
      });
    }
  }

  buscar(query: string) {
    this.searchQuery = query;
    this.aplicarFiltros();
  }

  cambiarAutor(nuevoAutor: string) {
    this.autorFilter = nuevoAutor;
    this.aplicarFiltros();
  }

  nextPage() {
    if (this.currentPage < this.pages) {
      this.loadLibros(this.currentPage + 1);
    }
  }

  previousPage() {
    if (this.currentPage > 1) {
      this.loadLibros(this.currentPage - 1)
    }
  }

}