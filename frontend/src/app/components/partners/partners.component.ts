import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-partners',
  standalone: true,
  imports: [CommonModule], // Para usar *ngFor
  templateUrl: './partners.component.html',
  styleUrls: ['./partners.component.css'],
})
export class PartnersComponent {
  logos = [
    'assets/img/andesmar_logo_color.png',
    'assets/img/andina_logo_color.jpg',
    'assets/img/inomax_logo_color.png',
    'assets/img/ombu_logo_color.png',
    'assets/img/porta_logo_color.png',
    'assets/img/tutu_logo_color.png',
    'assets/img/propato_logo_color.png',
  ];

  animationDuration = 60; // Duración animación en segundos
}
