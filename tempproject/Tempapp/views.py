from django.shortcuts import render
from .models import Employeess,Departmentss

# Create your views here.

def home(request):
    #emp=Employeess.objects.all()
    emp=Employeess.objects.all().select_related('department')
    print(emp)
    for i in emp:
        print(i.name,i.department.name)
    context={'res':emp}
    return render(request,'home1.html',context)