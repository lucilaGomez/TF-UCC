import { Component } from '@angular/core';
import { RouterModule } from '@angular/router'; // 👈 necesario para routerLink

@Component({
  selector: 'app-header',
  standalone: true,              // 👈 asegurate de declarar esto
  imports: [RouterModule],       // 👈 agregamos RouterModule acá
  templateUrl: './header.component.html',
  styleUrl: './header.component.css'
})
export class HeaderComponent { }
