"""loan_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from manager import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showHomeView, name='home'),
    # USER
    path('register/', views.registerUser, name='register'),
    path('accounts/login/', views.loginView, name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('users/edit/<int:pk>', views.editUser, name='edit-user'),
    path('users/delete/<int:pk>', views.deleteUser, name='delete-user'),
    path('users/<int:pk>', views.userDetailView, name='detail-view'),
    path('users/security/<int:pk>', views.editSecurity, name='security'),
    # ACCOUNT
    path('accounts/', views.accountListView, name='accounts'),
    path('accounts/<int:pk>', views.accountDetailView, name = 'detail-account'),
    path('accounts/create/', views.createAccount, name='create-account'),
    path('accounts/edit/<int:pk>', views.editAccount, name='edit-account'),
    path('accounts/delete/<int:pk>', views.deleteAccount, name='delete-account'),
    # CATEGORY
    path('categories/', views.categoryListView, name='categories'),
    path('categories/<int:pk>/', views.categoryDetailView, name='detail-category'),
    path('categories/create/', views.createCategory, name='create-category'),
    path('categories/edit/<int:pk>/', views.editCategory, name='edit-category'),
    path('categories/delete/<int:pk>/', views.deleteCategory, name='delete-category'),
    # BUDGET
    path('budgets/', views.budgetListView, name='budgets'),
    path('budgets/<int:pk>/', views.budgetDetailView, name='detail-budget'),
    path('budgets/create/', views.createBudget, name='create-budget'),
    path('budgets/edit/<int:pk>/', views.editBudget, name='edit-budget'),
    path('budgets/delete/<int:pk>/', views.deleteBudget, name='delete-budget'),


]
