
from django.urls import path

from Emploee.views import AddEmploy, listEmploy, EmployeLogin, Home, Profile

urlpatterns = [
path('add',AddEmploy,name='add'),
path('list',listEmploy,name='listEmploy'),
path('login',EmployeLogin,name='login'),
path('home',Home,name='home'),
path('profile',Profile,name='profile'),

]
