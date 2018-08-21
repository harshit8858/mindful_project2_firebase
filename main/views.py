from django.shortcuts import render, redirect
import firebase_admin
from firebase_admin import credentials, db
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
cred = credentials.Cert('C:\Users\Harshit Verma\Downloads\try-project-e4f24-6163c6fe2d67.json')
firebase_admin.initialize_app(cred, {
    'databaseURL' : "https://try-project-e4f24.firebaseio.com",
})
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
d_b = firebase.database()

root = db.reference()
new_user = root.child('users').push({
    'name': 'Admin1',
    'since': 1997
})

new_user.update({'since':1998})

admin1 = db.reference('user/{0}'.format(new_user.key)).get()
print('Name:',admin1['name'])
print('Since:',admin1['since'])

def login(request):
    return render(request, "main/login.html")


def home(request):
    order = Order.objects.all()
    email = request.POST.get('email')
    passw = request.POST.get("pass")
    try:
        user = auth.sign_in_with_email_and_password(email,passw)
    except:
        message = "invalid cerediantials"
        return render(request,"main/login.html",{"msg":message})
    print(user)
    return render(request, "main/home.html",{"email":email, 'order':order})


def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:home')
    else:
        form = OrderForm()
    return render(request, 'main/order.html', {'form':form})
