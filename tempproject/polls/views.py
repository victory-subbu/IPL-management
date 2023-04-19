from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Signin
from django.shortcuts import redirect
from django.contrib.auth import authenticate
#from polls.models import Department,Employee






def index(request):
    x=34+78
    context={
        "x":x,
        "name":"hello"
    }
    return render(request, 'index.html',context)
def shitij(request):
    return HttpResponse("<h1>Hello Shitij</h1>")

def auth(request):
    if(request.method=='POST'):
        print("this is post")
        name= request.POST['name']
        email=request.POST['email']
        password= request.POST['password']
        #print(name,password)
        ins=Signin(name=name,email=email,password=password)
        ins.save()
        print("data has go to db")
    return render(request,'login.html')
    
def login(request):
    if(request.method=='POST'):
        email=request.POST['email']
        password=request.POST['password']
        l=Signin.objects.filter(email=email,password=password)
        print(l)
        if(not l):
            return render(request,'login.html')
        else:
            return render(request,'sports.html')
    else:
        print(1)
        return HttpResponse("<h1>Hello Shitij</h1>")
    

def templogin(request):
    return render(request,'testlogin.html')

def testlogin(request):
    if(request.method=='POST'):
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        if(user is not None):
            return render(request,'main.html')
        else:
            return redirect('testlogin')
        



def setsession(request):  
    request.session['username'] = ''  
    request.session['password'] = 'subbu123@gmail.com'  
    return HttpResponse("session is set")  
def getsession(request):  
    studentname = request.session['username']  
    studentpassword = request.session['password']  
    return HttpResponse(studentname+" "+studentpassword);  
        
    
        




# Create your views here.
