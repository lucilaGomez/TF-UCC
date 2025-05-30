import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-user-config',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './user-config.component.html',
  styleUrls: ['./user-config.component.css']
})
export class UserConfigComponent {
  constructor(private router: Router) {}

  user = {
    firstName: '',
    lastName: '',
    gender: '',
    birthDate: '',
    cv: null as File | null
  };

  birthDateError = false;
  cvError = false;

  preventInvalidChars(event: KeyboardEvent): void {
    const allowed = /^[a-zA-ZÁÉÍÓÚÑáéíóúñ\s]$/;
    if (!allowed.test(event.key)) {
      event.preventDefault();
    }
  }

  sanitizeName(field: 'firstName' | 'lastName'): void {
    const input = this.user[field];
    this.user[field] = input.replace(/[^a-zA-ZÁÉÍÓÚÑáéíóúñ\s]/g, '');
  }

  hasInvalidChars(value: string): boolean {
    return /[^a-zA-ZÁÉÍÓÚÑáéíóúñ\s]/.test(value);
  }

  checkAge(): void {
    if (!this.user.birthDate) {
      this.birthDateError = false;
      return;
    }

    const birth = new Date(this.user.birthDate);
    const today = new Date();
    const age = today.getFullYear() - birth.getFullYear();
    const m = today.getMonth() - birth.getMonth();
    this.birthDateError = age < 18 || (age === 18 && m < 0);
  }

  onFileSelected(event: any): void {
    const file: File = event.target.files[0];
    if (!file) {
      this.cvError = true;
      return;
    }

    if (file.type !== 'application/pdf') {
      alert('Solo se permiten archivos PDF.');
      this.user.cv = null;
      this.cvError = true;
      event.target.value = '';
      return;
    }

    this.user.cv = file;
    this.cvError = false;
  }

  onSubmit(): void {
    if (this.birthDateError || this.cvError) return;

    this.router.navigate(['/my-user'], {
      state: { success: true, user: this.user }
    });
  }
}
