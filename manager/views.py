from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from .models import User
from .forms import UserCreateForm, UserRegistrationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm


def showHomeView(request):
    return render(request, "index.html")

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')

def registerUser(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            print('valid')
            form.save()
            return redirect('login')
        else:
            print(form.errors)
    form = UserRegistrationForm()
    return render(request, 'user_create.html', {'form': form})

def loginView(request):
    next_url = request.GET.get('next')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request=request, username=username, password=password)
            if user is not None:
                login(request, user)
                if next_url:
                    return redirect(next_url)
                else:
                    return redirect('home')
        else:
            print("ERRORS: ", form.errors)
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def userDetailView(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'user_detail.html', {'user': user})        

@login_required
def editUser(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST": 
        form = UserCreateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,'The user has been updated successfully!')
        return redirect('home')
    else:
        form = UserCreateForm(instance=user)
        return render(request,'edit_user.html', {'form': form})

def editSecurity(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == "POST": 
        form = UserCreationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,'The security has been updated successfully!')
        return redirect('home')
    else:
        form = UserCreationForm(instance=user)
        return render(request,'edit_user.html', {'form': form})

@login_required
def deleteUser(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    messages.success(request,  'The user has been deleted successfully!')
    return redirect('home')
