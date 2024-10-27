import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-abm',
  templateUrl: './abm.component.html',
  styleUrls: ['./abm.component.css']  // Corregido: styleUrl → styleUrls
})
export class AbmComponent {
  @Input() entidad!: 'usuario' | 'libro';  // Indica si es usuario o libro
  @Input() item_id: string = 'null';        // ID del elemento (usuario/libro)
  @Input() tipoOperacion!: string;          // Crear o Editar
}
