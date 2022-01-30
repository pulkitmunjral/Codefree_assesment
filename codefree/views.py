from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import flower
# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required
def add(request):
    if request.method == "POST":
        if 'action' in request.POST and request.POST['action']=="done":
            return redirect('profile')
        Sepal_length = request.POST['Sepal_length']
        Sepal_width = request.POST['Sepal_width']
        Petal_length = request.POST['Petal_length']
        Petal_width = request.POST['Petal_width']
        Class = request.POST['Class']
        ob=flower(Class=Class,Sepal_length=Sepal_length,Sepal_width=Sepal_width,Petal_length=Petal_length,Petal_width=Petal_width)
        ob.save()
        return redirect('profile')
    else:
        return render(request,"add.html")


@login_required
def profile(request):
    if request.method == "POST":
        if request.POST['action'] == "add":
            return redirect('add')
        if request.POST['action'] == "logout":
            return redirect('account_logout')
    else:
        return render(request, "profile.html")