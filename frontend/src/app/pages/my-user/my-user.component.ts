import { Component, ViewChild } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-my-user',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './my-user.component.html',
  styleUrls: ['./my-user.component.css']
})
export class MyUserComponent {
  user = {
    firstName: 'Juan',
    lastName: 'Pérez',
    gender: 'Masculino',
    birthDate: '1990-01-01',
    cvFileName: 'MiCV.pdf'
  };

  profileImageUrl: string | null = null;
  isLookingForJob = true;
  isEditing = false;

  tempUser = { ...this.user };
  tempCvFileName = this.user.cvFileName;

  @ViewChild('photoInput') photoInput: any;
  @ViewChild('cvInput') cvInput: any;

  triggerFileInput() {
    this.photoInput.nativeElement.click();
  }

  onPhotoSelected(event: Event): void {
    const input = event.target as HTMLInputElement;
    const file = input.files?.[0];
    if (file && file.type.startsWith('image/')) {
      const reader = new FileReader();
      reader.onload = () => {
        this.profileImageUrl = reader.result as string;
      };
      reader.readAsDataURL(file);
    } else {
      alert('Por favor seleccioná una imagen válida.');
    }
  }

  triggerCvUpload() {
    this.cvInput.nativeElement.click();
  }

  onCvSelected(event: Event): void {
    const input = event.target as HTMLInputElement;
    const file = input.files?.[0];
    if (file && file.type === 'application/pdf') {
      this.tempCvFileName = file.name;
    } else {
      alert('El archivo debe ser un PDF válido.');
    }
  }

  toggleJobStatus() {
    this.isLookingForJob = !this.isLookingForJob;
  }

  enableEdit() {
    this.tempUser = { ...this.user };
    this.tempCvFileName = this.user.cvFileName;
    this.isEditing = true;
  }

  saveChanges() {
    this.user = { ...this.tempUser, cvFileName: this.tempCvFileName };
    this.isEditing = false;
    alert('Cambios guardados correctamente.');
  }

  discardChanges() {
    this.isEditing = false;
    this.tempCvFileName = this.user.cvFileName;
  }
}
