import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-editusers',
  templateUrl: './editusers.component.html',
  styleUrl: './editusers.component.css'
})
export class EditusersComponent {
  usuario_id!: string;
  tipo_op!: string;
  constructor(
    private route:ActivatedRoute
  ) { }
  ngOnInit(): void {
    this.usuario_id = this.route.snapshot.paramMap.get('id') || '';
    this.tipo_op = this.route.snapshot.paramMap.get('tipo_op') || '';
    
    
    console.log('this.usuario_id: ',this.usuario_id);
    console.log('this.tipo_op: ',this.tipo_op);
  }
}