from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages, auth

# Create your views here.
def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        pswd = request.POST['password']

        
        user = auth.authenticate(request, username=username, password=pswd)
        if user is not None:
            auth.login(request, user)
            messages.success(request,"Welcome")
            return redirect("/list")
        else:
            messages.success(request,"Wrong Credentials Try Again")
            return redirect("login_page")
             
                
    return render(request, 'index.html')

def list(request):
    Targets = target.objects.all()

    context = {
        'tgs':Targets
        }
    return render(request, 'home.html',context)

def task(request):
    if request.method == 'POST':
        title = request.POST['title']
        Desc = request.POST['Desc']
        time = request.POST['time']
        status = request.POST['status']

        target.objects.create(title=title, Desc=Desc, time=time, status=status)

        return redirect("/list")
    return render(request, 'addnew.html')

def delete(request, id):
    targ = target.objects.get(id=id)
    targ.delete()
    return redirect("/list")