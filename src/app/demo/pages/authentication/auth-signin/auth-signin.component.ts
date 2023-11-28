import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule ,Router } from '@angular/router';

@Component({
  selector: 'app-auth-signin',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './auth-signin.component.html',
  styleUrls: ['./auth-signin.component.scss'],
})
export default class AuthSigninComponent {
  constructor(private router: Router) { }

  navigateToDashboard() {
    // Navigate to the 'dashboard' route and replace the current history entry
    this.router.navigate(['/dashboard'], { skipLocationChange: true });
  }
}
