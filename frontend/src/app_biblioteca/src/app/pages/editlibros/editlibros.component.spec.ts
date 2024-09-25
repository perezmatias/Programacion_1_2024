import { ComponentFixture, TestBed } from '@angular/core/testing';

import { EditlibrosComponent } from './editlibros.component';

describe('EditlibrosComponent', () => {
  let component: EditlibrosComponent;
  let fixture: ComponentFixture<EditlibrosComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [EditlibrosComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(EditlibrosComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
