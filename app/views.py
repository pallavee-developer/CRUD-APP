from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password,check_password
from .models import User


# Create your views here.
def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request,'login.html')

def user_login(request):
    if request.method =='POST':
        email= request.POST['email']
        user_psw = request.POST['psw']
        if User.objects.filter(email = email).exists():
            obj= User.objects.get(email=email)
            pwd=obj.psw
            if check_password(user_psw,pwd):
                return redirect('/welcome/')
            else:
                return HttpResponse("<h1>Incorrect Password</h1>")
    else:
        return HttpResponse("<h1>Email not register</h1>")

def data(request):
    user_obj= User.objects.all()
    return render(request,'table.html',{'user_obj':user_obj})   


def registration(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        psw = make_password(request.POST['psw'])
        if User.objects.filter(email=email).exists():
            return HttpResponse('<h1>Email Already Exist</h1>')
        else:
            User.objects.create(name=name, email=email, psw=psw)
            return redirect('/login/')

def welcome(request):
    return (request, 'welcome.html')


def deletedata(request):
    id=request.GET['id']
    User.objects.get(id=id).delete()
    return render('/data')

def update(request,uid):
    user=User.objects.get(id=uid)
    return render()

def update_data(request):
    if request.method== "POST":
        uid=request.POST['uid']
        name=request.POST['name']
        email=request.POST['email']