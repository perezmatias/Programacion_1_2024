import { Component } from '@angular/core';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-configuracion',
  templateUrl: './configuracion.component.html',
  styleUrl: './configuracion.component.css'
})
export class ConfiguracionComponent {

    constructor(
      private authService: AuthService
    ) {}

    cerrarSesion() {
      this.authService.logout();
    }
}
