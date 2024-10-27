import { Component } from '@angular/core';
import { AuthService } from '../../services/auth.service';

@Component({
  selector: 'app-nav',
  templateUrl: './nav.component.html',
  styleUrl: './nav.component.css'
})
export class NavComponent {
  
  constructor(
    private authService: AuthService
  ) {}

  cerrarSesion() {
    this.authService.logout();
  }

}
