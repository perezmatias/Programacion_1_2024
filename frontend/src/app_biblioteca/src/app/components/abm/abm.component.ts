import { Component, Input } from '@angular/core';
import { UsuarioService } from '../../services/usuario.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-abm',
  templateUrl: './abm.component.html',
  styleUrls: ['./abm.component.css']
})
export class AbmComponent {
  @Input() entidad!: 'usuario' | 'libro' | 'prestamo';
  @Input() item_id: string = 'null';
  @Input() tipoOperacion!: string;
  usuario: any = {}; // Para almacenar los datos a editar

  constructor(private usuarioService: UsuarioService, private router:Router) {}

  saveChanges() {
    if (this.item_id !== 'null') {
      this.usuarioService.updateUser(this.item_id, this.usuario).subscribe(response => {
        console.log('Usuario actualizado', response);
        this.router.navigate(['/usuarios']);
        // Aquí puedes redirigir o mostrar un mensaje de éxito
      });
    }
  }

  cancel() {
    this.router.navigate(['/usuarios']);
  }
}
