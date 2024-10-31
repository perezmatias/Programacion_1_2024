import { ChangeDetectorRef, Component } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { LibroService } from '../../services/libro.service';

@Component({
  selector: 'app-editlibros',
  templateUrl: './editlibros.component.html',
  styleUrl: './editlibros.component.css'
})
export class EditlibrosComponent {
  libro_id!: string;
  tipo_op!: string;
  libro: any= {
    nombre: '',
    genero: '',
    cant_ejemplares: '' ,
  }

  constructor(
    private route:ActivatedRoute,
    private libroService: LibroService,
    private cdr: ChangeDetectorRef
  ) { }

  ngOnInit(): void {
    this.libro_id = this.route.snapshot.paramMap.get('id') || '';
    this.tipo_op = this.route.snapshot.paramMap.get('tipo_op') || '';

    if (this.libro_id !== 'null') {
      this.libroService.getLibroById(this.libro_id).subscribe((data: any) => {
        this.libro = data;
        this.cdr.detectChanges();
      })
    }
  }
}
