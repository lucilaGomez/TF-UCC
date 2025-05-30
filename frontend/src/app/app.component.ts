import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { HeaderComponent } from './components/header/header.component';
import { HeroComponent } from './components/hero/hero.component';
import { PartnersComponent } from './components/partners/partners.component';
import { FeaturesComponent } from './components/features/features.component';
import { TestimonialsComponent } from './components/testimonials/testimonials.component';
import { FooterComponent } from './components/footer/footer.component';
import { LoginComponent } from './components/login/login.component';
import { ReactiveFormsModule } from '@angular/forms'; // 👈 NECESARIO
import { UserConfigComponent } from './pages/user-config/user-config.component';
import { MyUserComponent } from './pages/my-user/my-user.component';
@Component({
  selector: 'app-root',
  standalone: true,
  imports: [
    RouterOutlet,
    ReactiveFormsModule,       
    HeaderComponent,
    HeroComponent,
    PartnersComponent,
    FeaturesComponent,
    TestimonialsComponent,
    FooterComponent,
    LoginComponent,
    UserConfigComponent,
    MyUserComponent,
  ],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'tf-frontend';
}
