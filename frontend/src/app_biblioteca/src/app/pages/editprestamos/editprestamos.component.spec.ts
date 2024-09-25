import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EditprestamosComponent } from './editprestamos.component';

describe('EditprestamosComponent', () => {
  let component: EditprestamosComponent;
  let fixture: ComponentFixture<EditprestamosComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [EditprestamosComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(EditprestamosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
