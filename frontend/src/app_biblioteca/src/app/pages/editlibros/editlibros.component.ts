import { Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-editlibros',
  templateUrl: './editlibros.component.html',
  styleUrl: './editlibros.component.css'
})
export class EditlibrosComponent {
  libro_id!: string;
  tipo_op!: string;
  constructor(
    private route:ActivatedRoute
  ) { }
  ngOnInit(): void {
    this.libro_id = this.route.snapshot.paramMap.get('id') || '';
    this.tipo_op = this.route.snapshot.paramMap.get('tipo_op') || '';
    
    
    console.log('this.libro_id: ',this.libro_id);
    console.log('this.tipo_op: ',this.tipo_op);
  }
}
