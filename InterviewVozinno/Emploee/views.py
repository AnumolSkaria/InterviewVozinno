from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView

from Emploee.forms import EmployeeCreate, EmployLogin
from Emploee.models import Employee

#
# class AddEmploy(CreateView):
#     model = Employee
#     form_class=EmployeeCreate
#     template_name = 'create_employ.html'
#     success_url = reverse_lazy('add')


def AddEmploy(request):
    form=EmployeeCreate()
    template_name='create_employ.html'
    context={}
    context["form"]=form
    if request.method=='POST':
        form=EmployeeCreate(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request,template_name,context)

def listEmploy(request):
    template_name='list_employ.html'
    qs=Employee.objects.all()
    context={}
    context["queryset"]=qs
    return render(request,template_name,context)

def EmployeLogin(request):
    form=EmployLogin()
    template_name="login.html"
    context={}
    context["form"]=form
    if request.method=='POST':
        username=request.POST.get("User_name")
        print(username)
        password=request.POST.get("Password")
        qs=Employee.objects.get(User_name=username)
        if (qs):
            if (password == qs.Password):
                print("ok")
                print("successfully Login")
                context={}
                context['user']=username
                # return redirect("profile")
                return render(request,'profile.html',context)
            else:
                return render("login.html")
    return render(request, template_name, context)


def Home(request):
    template_name='home.html'
    qs=Employee.objects.all()
    context={}
    context["emp"]=qs
    return render(request,template_name)

def Profile(request):
    template_name='profile.html'
    # qs=Employee.objects.get(User_name=username)
    # print(qs)
    # context={}
    # context["book"]=qs
    return render(request,template_name)