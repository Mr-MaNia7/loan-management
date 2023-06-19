from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from manager.forms import UserCreateForm

class Command(BaseCommand):
    help = 'Seed data for User model'

    def handle(self, *args, **options):
        User = get_user_model()
        form = UserCreationForm()
        users = [
            {
                'username': 'john_doe',
                'email': 'johndoe@example.com',
                'first_name': 'John',
                'last_name': 'Doe',
                'password1': make_password('pwmania@5304'),
                'password2': make_password('pwmania@5304'),
            },
            # Add more user data as needed
        ]

        for user_data in users:
            form = UserCreateForm(user_data)
            if form.is_valid():
                user = form.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully created user: {user.username}'))
            else:
                self.stdout.write(self.style.ERROR(f'Failed to create user: {user_data["username"]}'))
