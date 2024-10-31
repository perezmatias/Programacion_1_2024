import { Component, input, Input, OnInit } from '@angular/core';
import { UsuarioService } from '../../services/usuario.service';
import { LibroService } from '../../services/libro.service';
import { PrestamoService } from '../../services/prestamo.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-abm',
  templateUrl: './abm.component.html',
  styleUrls: ['./abm.component.css']
})
export class AbmComponent implements OnInit {
  @Input() entidad!: 'usuario' | 'libro' | 'prestamo';
  @Input() item_id: string = 'null';
  @Input() tipoOperacion!: string;
  @Input() usuario: any = {}; // Para almacenar los datos a editar
  @Input() libro: any = {}
  @Input() prestamo: any = {}

  constructor(
    private usuarioService: UsuarioService,
    private router:Router,
    private libroService: LibroService,
    private prestamoService: PrestamoService
  ) {}

  ngOnInit() {
    if (this.item_id !== 'null') {
      if (this.entidad === 'usuario') {
        this.usuarioService.getUserById(this.item_id).subscribe((data: any) => {
          this.usuario = data;
        });
      } else if (this.entidad === 'libro') {
        this.libroService.getLibroById(this.item_id).subscribe((data: any) => {
          this.libro = data;
        });
      } else if (this.entidad === 'prestamo') {
        this.prestamoService.getPrestamoById(this.item_id).subscribe((data: any) => {
          this.prestamo = data;
        });
      }
      // Agrega lógica similar para 'libro' y 'prestamo' si es necesario
    }
  }

  get password(): string {
    return this.usuario.contraseña;
  }

  set password(value: string) {
    this.usuario.contraseña = value;
  }
  
  saveChanges() {
    if (this.entidad === 'usuario') {
      if (this.item_id === 'null') {
        // Lógica para crear un usuario
        this.usuarioService.createUser(this.usuario).subscribe(response => {
          console.log('Usuario creado', response);
          this.router.navigate(['/usuarios']); // Redirige a la lista de usuarios
        });
      } else {
        // Lógica para actualizar un usuario existente
        this.usuarioService.updateUser(this.item_id, this.usuario).subscribe(response => {
          console.log('Usuario actualizado', response);
          this.router.navigate(['/usuarios']); // Redirige a la lista de usuarios
        });
      }
    } else if (this.entidad === 'libro') {
      if (this.item_id === 'null') {
        // Lógica para crear un libro
        this.libroService.createLibro(this.libro).subscribe(response => {
          console.log('Libro creado', response);
          this.router.navigate(['/libros']); // Redirige a la lista de libros
        });
      } else {
        // Lógica para actualizar un libro existente
        this.libroService.updateLibro(this.item_id, this.libro).subscribe(response => {
          console.log('Libro actualizado', response);
          this.router.navigate(['/libros']); // Redirige a la lista de libros
        });
      } 
    } else if (this.entidad === 'prestamo') {
      if (this.item_id === 'null') {
        // Lógica para crear un libro
        this.prestamoService.createPrestamo(this.prestamo).subscribe(response => {
          console.log('Prestamo creado', response);
          this.router.navigate(['/prestamos']); // Redirige a la lista de libros
        });
      } else {
        // Lógica para actualizar un libro existente
        this.prestamoService.updatePrestamo(this.item_id, this.prestamo).subscribe(response => {
          console.log('Prestamo actualizado', response);
          this.router.navigate(['/prestamos']); // Redirige a la lista de libros
        });
      }
    }
  }
    
  cancel() {
    if (this.entidad === 'usuario') {
      this.router.navigate(['/usuarios']); // Redirige a la lista de usuarios
    } else if (this.entidad === 'libro') {
      this.router.navigate(['/libros']); // Redirige a la lista de libros
    } else if (this.entidad === 'prestamo') {
      this.router.navigate(['/prestamos']);
    }
  }
}
