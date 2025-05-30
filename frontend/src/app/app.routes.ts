import { Routes } from '@angular/router';
import { LoginComponent } from './components/login/login.component';
import { LandingComponent } from './components/landing/landing.component';
import { RegisterComponent } from './components/register/register.component';
import { UserConfigComponent } from './pages/user-config/user-config.component';
import { MyUserComponent } from './pages/my-user/my-user.component';

export const routes: Routes = [
  { path: '', component: LandingComponent },
  { path: 'login', component: LoginComponent },
  { path: 'register', component: RegisterComponent },
  { path: 'user-config', component: UserConfigComponent },
  { path: 'my-user', component: MyUserComponent }
];
