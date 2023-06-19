from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


def showHomeView(request):
    return render(request, "index.html")

def registerUser(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
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

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')

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
        return render(request,'user_edit.html', {'form': form})

@login_required
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
        return render(request,'user_edit.html', {'form': form})

@login_required
def deleteUser(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    messages.success(request,  'The user has been deleted successfully!')
    return redirect('home')

@login_required
def createAccount(request):
    form = AccountCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            post = form.save()
            post.user_id = request.user
            post.save()
            messages.success(request,'The Account has been created successfully!')
            return redirect('accounts')
    else:
        form = AccountCreationForm()
    
    return render(request, 'account_create.html', {'form': form})

@login_required
def editAccount(request, pk):
    account = get_object_or_404(Account, pk=pk)
    if request.method == 'POST':
        form = AccountCreationForm(request.POST, instance=account)
        if form.is_valid():
            post = form.save()
            post.user_id = request.user
            messages.success(request,'The account has been updated successfully!')
            post.save()
            return redirect('accounts')
    else:
        form = AccountCreationForm(instance=account)
    
    return render(request, 'account_edit.html', {'form': form})

@login_required
def accountListView(request):
    accounts = Account.objects.all()
    return render(request, 'account_list.html', {'accounts': accounts})

@login_required
def deleteAccount(request, pk):
    account = get_object_or_404(Account, pk=pk)
    account.delete()
    messages.success(request,  'The user has been deleted successfully!')
    return redirect('accounts')

@login_required
def accountDetailView(request, pk):
    account = get_object_or_404(Account, pk=pk)
    return render(request, 'account_detail.html', {'account': account}) 