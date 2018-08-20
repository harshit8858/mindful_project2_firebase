from django.shortcuts import render
import pyrebase

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

def login(request):
    return render(request, "main/login.html")


def home(request):
    email = request.POST.get('email')
    passw = request.POST.get("pass")
    try:
        user = auth.sign_in_with_email_and_password(email,passw)
    except:
        message = "invalid cerediantials"
        return render(request,"main/login.html",{"msg":message})
    print(user)
    return render(request, "main/home.html",{"email":email})
