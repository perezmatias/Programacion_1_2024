import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class LibroService {
  url = '/api';
  
  constructor(private httpClient: HttpClient) {}

  getLibros(page: number = 1, perPage: number = 10): Observable<any> {
    let auth_token = localStorage.getItem('token');
    let headers = new HttpHeaders({
      'Content-type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });
    const requestOptions = { headers: headers };

    return this.httpClient.get(`${this.url}/libros?page=${page}&per_page=${perPage}`, requestOptions);
  }

  getLibroById(id: string) {
    let auth_token = localStorage.getItem('token');
    let headers = new HttpHeaders({
      'Content-type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });
    const requestOptions = { headers: headers };

    return this.httpClient.get(`${this.url}/libro/${id}`, requestOptions);
  }

  createLibro(libroData: any) {
    const auth_token = localStorage.getItem('token');
    const headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });
    const requestOptions = { headers: headers };
  
    return this.httpClient.post(`${this.url}/libros`, libroData, requestOptions);
  }

  updateLibro(id: string, libroData: any) {
    let auth_token = localStorage.getItem('token');
    let headers = new HttpHeaders({
      'Content-type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });
    const requestOptions = { headers: headers };

    return this.httpClient.put(`${this.url}/libro/${id}`, libroData, requestOptions);
  }

  deleteLibro(id: string) {
    let auth_token = localStorage.getItem('token');
    let headers = new HttpHeaders({
      'Content-type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });
    const requestOptions = { headers: headers };

    return this.httpClient.delete(`${this.url}/libro/${id}`, requestOptions);
  }
}