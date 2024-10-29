import { ChangeDetectorRef, Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { UsuarioService } from '../../services/usuario.service';

@Component({
  selector: 'app-editusers',
  templateUrl: './editusers.component.html',
  styleUrls: ['./editusers.component.css']
})
export class EditusersComponent implements OnInit {
  usuario_id!: string;
  tipo_op!: string;
  usuario: any = {
    nombre: '',
    apellido: '',
    email: '',
    telefono: '',
    rol: ''
  }; // Para almacenar los datos del usuario

  constructor(
    private route: ActivatedRoute,
    private usuarioService: UsuarioService,
    private cdr: ChangeDetectorRef
  ) { }

  ngOnInit(): void {
    this.usuario_id = this.route.snapshot.paramMap.get('id') || '';
    this.tipo_op = this.route.snapshot.paramMap.get('tipo_op') || '';

    if (this.usuario_id !== 'null') {
      // Cargar los datos del usuario si el ID no es 'null'
      this.usuarioService.getUserById(this.usuario_id).subscribe((data: any) => {
        this.usuario = data;
        this.cdr.detectChanges();
      });
    }
  }
}
