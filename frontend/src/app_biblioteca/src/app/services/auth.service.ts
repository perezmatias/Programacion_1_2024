import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, take } from 'rxjs';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  url = '/api';
  constructor(
    private httpClient: HttpClient,
    private router: Router
  ) { }

  login(dataLogin:any): Observable<any> {
  //  let dataLogin = {
  //  email: "admin@example.com",
  //  contraseña: "admin1"
  //  }

    return this.httpClient.post(this.url+'/auth/login',dataLogin).pipe(take(1));
    
  }

  logout() {
    localStorage.removeItem('token')
    this.router.navigateByUrl('login')
  }
}
