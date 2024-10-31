import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { PrestamoService } from '../../services/prestamo.service';

@Component({
  selector: 'app-editprestamos',
  templateUrl: './editprestamos.component.html',
  styleUrl: './editprestamos.component.css'
})
export class EditprestamosComponent implements OnInit {
  prestamo_id!: string;
  tipo_op!: string;
  prestamo: any = {
    Fecha_devolucion: '',
    Fecha_retiro: '',
    id_usuario: '',
    libros: []
  };

  constructor(
    private route:ActivatedRoute,
    private prestamoService: PrestamoService,

  ) { }
  ngOnInit(): void {
    this.prestamo_id = this.route.snapshot.paramMap.get('id') || '';
    this.tipo_op = this.route.snapshot.paramMap.get('tipo_op') || '';
    
    if(this.prestamo_id !== 'null'){
      this.prestamoService.getPrestamoById(this.prestamo_id).subscribe((data: any) => {
        this.prestamo = data;
      });
    }
  }
}