import { ComponentFixture, TestBed } from '@angular/core/testing';
import { PartnersComponent } from './partners.component';

describe('PartnersComponent', () => {
  let component: PartnersComponent;
  let fixture: ComponentFixture<PartnersComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [PartnersComponent]  // Importar el componente standalone aquí
    }).compileComponents();

    fixture = TestBed.createComponent(PartnersComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create the partners component', () => {
    expect(component).toBeTruthy();
  });

  it('should have logos array defined', () => {
    expect(component.logos).toBeDefined();
    expect(component.logos.length).toBeGreaterThan(0);
  });
});
