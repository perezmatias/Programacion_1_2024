import { ComponentFixture, TestBed } from '@angular/core/testing';

import { LibrosuserComponent } from './librosuser.component';

describe('LibrosuserComponent', () => {
  let component: LibrosuserComponent;
  let fixture: ComponentFixture<LibrosuserComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [LibrosuserComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(LibrosuserComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
