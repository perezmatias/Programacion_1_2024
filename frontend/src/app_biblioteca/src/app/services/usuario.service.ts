import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';


@Injectable({
  providedIn: 'root'
})
export class UsuarioService {
  url = '/api';
  constructor(
    private httpClient:HttpClient
  ) { }


  getUsers() {
    let auth_token = localStorage.getItem('token');

    let headers = new HttpHeaders ({
      'Content-type': 'application/json',
      'Authorization': `Bearer $(auth_token)`
    })

    const requestOptions = {headers: headers}

    return this.httpClient.get(this.url + '/usuarios', requestOptions);
  }
}
