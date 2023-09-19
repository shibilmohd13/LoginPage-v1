from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from django.views.decorators.cache import cache_control
from login.models import Users


# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def signup(request):
    if 'username' in request.session:
        return redirect(dashboard)

    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username is taken")
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email is already registered")
            return redirect('signup')
        elif len(password) < 4:
            messages.error(request, "Password must be More than 4 characters")
            return redirect('signup')
        elif password!=confirm_password:
            messages.error(request, "Passwords does not match")
            return redirect('signup')
        else:
            user = User.objects.create_user(username, email, password)
            user.save()
            messages.success(request, "User created successfully")
            return redirect('login')
    else:
        return render(request, "signup.html")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):
    if 'username' in request.session:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            request.session['username'] = username
            return redirect('dashboard')
        else:
            messages.error(request, "invalid user")
            return redirect('login')
    else:
        return render(request, "login.html")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dashboard(request):
    if 'username' in request.session:
        username = request.session['username']
        return render(request, "dashboard.html", {'username':username})
    else:
        return redirect('login')


    
def logout(request):
    if 'username' in request.session:
        request.session.flush()
    return redirect('login')

def adminlogin(request):
    return render(request, 'adminlogin.html')

def admindash(request):
    obj = Users.objects.all()
    context = {
        "obj" :obj,
    }
    return render(request, "admin.html", context)

def add(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = Users(
            username = username,
            email = email,
            password = password,
        )
        user.save()
        return redirect('admindash')
    return render(request, 'admin.html')

def edit(request):
    obj = Users.objects.all()

    context = {
        'obj' : obj
    }
    return redirect(request, 'admindash.html',context)

def update(request, id):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]

        obj = Users(
            id = id,
            username = username,
            email = email,
            password = password,
        )
        obj.save()
        return redirect('admindash')

    return redirect(request, 'admindash.html')

def delete(request, id):
    obj = Users.objects.filter(id=id)
    obj.delete()
    context = {
        "obj" : obj, 
    }
    return redirect("admindash")
