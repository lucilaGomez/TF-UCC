import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

interface Testimonial {
  name: string;
  role: string;
  image: string;
  rating: number;
  text: string;
}

@Component({
  selector: 'app-testimonials',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './testimonials.component.html',
  styleUrls: ['./testimonials.component.css']
})
export class TestimonialsComponent {
  visibleTestimonials: Testimonial[] = [
    {
      name: 'Leo',
      role: 'Lead Designer',
      image: 'https://randomuser.me/api/portraits/men/1.jpg',
      rating: 4,
      text: 'It was a very good experience.'
    },
    {
      name: 'Anna',
      role: 'Project Manager',
      image: 'https://randomuser.me/api/portraits/women/2.jpg',
      rating: 5,
      text: 'Amazing support and professionalism throughout the project.'
    },
    {
      name: 'John',
      role: 'Developer',
      image: 'https://randomuser.me/api/portraits/men/3.jpg',
      rating: 3,
      text: 'Good collaboration but can improve in communication.'
    }
  ];
}
