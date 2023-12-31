from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return  redirect('/')
        else:
            messages.info(request,"invalid massapp")
            return  redirect('login')
    return render(request,"login.html")
def creatine(request):
    if request.method=="POST":
        username=request.POST['username']
        sname=request.POST['first_name']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('creatine')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email exists')
                return redirect('creatine')
            else:

                user=User.objects.create_user(username=username,password=password,first_name=sname)
                user.save()
                print("user created")
                return redirect('login')
        else:
             messages.info(request,"password not matched")
             return redirect('creatine')
        return redirect('/')

    return render(request,"mass.html")
def logout(request):
    auth.logout(request)
    return redirect('/')