import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class PrestamoService {
  url = '/api';

  constructor(private httpClient: HttpClient) {}

  getPrestamos(page: number = 1, per_page: number = 10): Observable<any> {
    let auth_token = localStorage.getItem('token');
    let headers = new HttpHeaders({
      'Content-type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });
    const requestOptions = { headers: headers };

    return this.httpClient.get(`${this.url}/prestamos?page=${page}&per_page=${per_page}`, requestOptions);
  }

  deletePrestamos(id:string) {
    let auth_token = localStorage.getItem('token')
    let headers = new HttpHeaders({
      'Content-type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });
    const requestOptions = { headers:headers};

    return this.httpClient.delete(`${this.url}/prestamo/${id}`, requestOptions);
  }

  getPrestamoById(id: string) {
    let auth_token = localStorage.getItem('token');
    let headers = new HttpHeaders({
      'Content-type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });
    const requestOptions = { headers: headers };

    return this.httpClient.get(`${this.url}/prestamo/${id}`, requestOptions);
  }

  updatePrestamo(id: string, userData: any) {
    let auth_token = localStorage.getItem('token');
    let headers = new HttpHeaders({
      'Content-type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });
    const requestOptions = { headers: headers };

    return this.httpClient.put(`${this.url}/prestamo/${id}`, userData, requestOptions);
  }

  createPrestamo(userData: any) {
    const auth_token = localStorage.getItem('token');
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });
    const requestOptions = { headers: headers };
  
    return this.httpClient.post('/api/prestamos', userData, requestOptions);
  }

}
