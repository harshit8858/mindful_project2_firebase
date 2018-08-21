from django.shortcuts import render, redirect
from django.http import HttpResponse

import pyrebase
from .forms import *

config = {
    'apiKey' : "AIzaSyAa8s8VsFeVlIy0-oVipgHfQxwxqlNv6jg",
    'authDomain' : "try-project-e4f24.firebaseapp.com",
    'databaseURL' : "https://try-project-e4f24.firebaseio.com",
    'projectId' : "try-project-e4f24",
    'storageBucket' : "try-project-e4f24.appspot.com",
    'messagingSenderId' : "864587093826"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

def login(request):
    return render(request, "main/login.html")


def home(request):
    order = Order.objects.all()
    email = request.POST.get('email')
    passw = request.POST.get("pass")
    try:
        u = auth.sign_in_with_email_and_password(email,passw)
    except:
        message = "invalid cerediantials"
        return render(request,"main/login.html",{"msg":message})
    print(u)
    data = {
        "name": "Mortimer 'Morty' Smith"
    }
    results = db.child("us").push(data, u['idToken'])
    return render(request, "main/home.html",{"email":email, 'order':order, 'data':data, 'result':results})


def try1(request):
    data = {
        "name": "Mortimer 'Morty' Smith"
    }
    results = db.child("users").push(data, u['idToken'])
    return render(request, 'main/try1.html', {'data':data, 'result':results})


def order(request):
    order1 = db.child("Order").get().val()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:home')
    else:
        form = OrderForm()
    return render(request, 'main/order.html', {'form':form, 'order1':order1})
