import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class UsuarioService {
  url = '/api';
  
  constructor(private httpClient: HttpClient) {}

  getUsers() {
    let auth_token = localStorage.getItem('token');
    let headers = new HttpHeaders({
      'Content-type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });
    const requestOptions = { headers: headers };

    return this.httpClient.get(this.url + '/usuarios', requestOptions);
  }

  deleteUser(id:string) {
    let auth_token = localStorage.getItem('token')
    let headers = new HttpHeaders({
      'Content-type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });
    const requestOptions = { headers:headers};

    return this.httpClient.delete(`${this.url}/usuario/${id}`, requestOptions);
  }

  getUserById(id: string) {
    let auth_token = localStorage.getItem('token');
    let headers = new HttpHeaders({
      'Content-type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });
    const requestOptions = { headers: headers };

    return this.httpClient.get(`${this.url}/usuario/${id}`, requestOptions);
  }

  updateUser(id: string, userData: any) {
    let auth_token = localStorage.getItem('token');
    let headers = new HttpHeaders({
      'Content-type': 'application/json',
      'Authorization': `Bearer ${auth_token}`
    });
    const requestOptions = { headers: headers };

    return this.httpClient.put(`${this.url}/usuario/${id}`, userData, requestOptions);
  }
}
