import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-editprestamos',
  templateUrl: './editprestamos.component.html',
  styleUrl: './editprestamos.component.css'
})
export class EditprestamosComponent {
  prestamo_id!: string;
  tipo_op!: string;
  constructor(
    private route:ActivatedRoute
  ) { }
  ngOnInit(): void {
    this.prestamo_id = this.route.snapshot.paramMap.get('id') || '';
    this.tipo_op = this.route.snapshot.paramMap.get('tipo_op') || '';
    
    
    console.log('this.prestamo_id: ',this.prestamo_id);
    console.log('this.tipo_op: ',this.tipo_op);
  }
}