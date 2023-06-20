from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


def showHomeView(request):
    accounts = Account.objects.all()
    context = {'accounts': accounts}
    return render(request, "index.html", context)

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

# ACCOUNT
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

# CATEGORY
@login_required
def createCategory(request):
    form = CategoryCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            messages.success(request, 'The Category has been created successfully!')
            return redirect('categories')
    else:
        form = CategoryCreationForm()
    
    return render(request, 'category_create.html', {'form': form})

@login_required
def editCategory(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryCreationForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            messages.success(request, 'The category has been updated successfully!')
            return redirect('categories')
    else:
        form = CategoryCreationForm(instance=category)
    
    return render(request, 'category_edit.html', {'form': form})

@login_required
def categoryListView(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

@login_required
def deleteCategory(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    messages.success(request, 'The category has been deleted successfully!')
    return redirect('categories')

@login_required
def categoryDetailView(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'category_detail.html', {'category': category})

# BUDGET
@login_required
def createBudget(request):
    if request.method == 'POST':
        form = BudgetCreationForm(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            budget.save()
            messages.success(request, 'The budget has been created successfully!')
            return redirect('budgets')
    else:
        form = BudgetCreationForm()
    
    return render(request, 'budget_create.html', {'form': form})

@login_required
def editBudget(request, pk):
    budget = get_object_or_404(Budget, pk=pk)
    if request.method == 'POST':
        form = BudgetCreationForm(request.POST, instance=budget)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            budget.save()
            messages.success(request, 'The budget has been updated successfully!')
            return redirect('budgets')
    else:
        form = BudgetCreationForm(instance=budget)
    
    return render(request, 'budget_edit.html', {'form': form})

@login_required
def budgetListView(request):
    budgets = Budget.objects.all()
    return render(request, 'budget_list.html', {'budgets': budgets})

@login_required
def deleteBudget(request, pk):
    budget = get_object_or_404(Budget, pk=pk)
    budget.delete()
    messages.success(request, 'The budget has been deleted successfully!')
    return redirect('budgets')

@login_required
def budgetDetailView(request, pk):
    budget = get_object_or_404(Budget, pk=pk)
    return render(request, 'budget_detail.html', {'budget': budget})

# TRANSACTION
@login_required
def transactionListView(request):
    transactions = Transaction.objects.all()
    return render(request, 'transaction_list.html', {'transactions': transactions})

@login_required
def createTransaction(request):
    form = TransactionCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            transaction = form.save()
            messages.success(request, 'The transaction has been created successfully!')
            return redirect('transactions')
    else:
        form = TransactionCreationForm()
    
    return render(request, 'transaction_create.html', {'form': form})

@login_required
def editTransaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        form = TransactionCreationForm(request.POST, instance=transaction)
        if form.is_valid():
            transaction = form.save()
            messages.success(request, 'The transaction has been updated successfully!')
            return redirect('transactions')
    else:
        form = TransactionCreationForm(instance=transaction)
    
    return render(request, 'transaction_edit.html', {'form': form})

@login_required
def deleteTransaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    transaction.delete()
    messages.success(request, 'The transaction has been deleted successfully!')
    return redirect('transactions')

@login_required
def transactionDetailView(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    return render(request, 'transaction_detail.html', {'transaction': transaction})
# GOAL
@login_required
def goalListView(request):
    goals = Goal.objects.all()
    return render(request, 'goal_list.html', {'goals': goals})

@login_required
def createGoal(request):
    form = GoalCreationForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            goal = form.save()
            messages.success(request, 'The goal has been created successfully!')
            return redirect('goals')
    else:
        form = GoalCreationForm()
    
    return render(request, 'goal_create.html', {'form': form})

@login_required
def editGoal(request, pk):
    goal = get_object_or_404(Goal, pk=pk)
    if request.method == 'POST':
        form = GoalCreationForm(request.POST, instance=goal)
        if form.is_valid():
            goal = form.save()
            messages.success(request, 'The goal has been updated successfully!')
            return redirect('goals')
    else:
        form = GoalCreationForm(instance=goal)
    
    return render(request, 'goal_edit.html', {'form': form})

@login_required
def deleteGoal(request, pk):
    goal = get_object_or_404(Goal, pk=pk)
    goal.delete()
    messages.success(request, 'The goal has been deleted successfully!')
    return redirect('goals')

@login_required
def goalDetailView(request, pk):
    print('YES')
    goal = get_object_or_404(Goal, pk=pk)
    return render(request, 'goal_detail.html', {'goal': goal})
