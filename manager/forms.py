from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.forms import DateInput


class UserCreateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class AccountCreationForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name', 'type', 'balance', 'interest_rate', 'user_id']

class CategoryCreationForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['user', 'name', 'parent']

class BudgetCreationForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['user', 'category', 'amount', 'start_date', 'end_date']
        widgets = {
            'start_date': DateInput(attrs={'type': 'date'}),
            'end_date': DateInput(attrs={'type': 'date'}),
        }

