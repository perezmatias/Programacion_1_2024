import { Component, input, Input, OnInit } from '@angular/core';
import { UsuarioService } from '../../services/usuario.service';
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

  constructor(private usuarioService: UsuarioService, private router:Router) {}

  ngOnInit() {
    if (this.item_id !== 'null') {
      if (this.entidad === 'usuario') {
        this.usuarioService.getUserById(this.item_id).subscribe((data: any) => {
          this.usuario = data;
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
  }

  cancel() {
    this.router.navigate(['/usuarios']);
  }
}
