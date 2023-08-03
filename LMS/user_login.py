from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from app.EmailBackEnd import EmailBackEnd
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def REGISTER(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check email
        if User.objects.filter(email=email).exists():
            messages.warning(request, 'Email Already Exists!')
            return redirect('register')

        # Check username
        if User.objects.filter(username=username).exists():
            messages.warning(request, 'Username Already Exists!')
            return redirect('register')

        user = User.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.save()
        return redirect('login')

    return render(request, 'registration/register.html')

def DO_LOGIN(request):
    username= request.POST["username"]
    password= request.POST["password"]
        ## email = request.POST.get('email')
        ## password = request.POST.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        messages.error(request, 'Email and Password Are Invalid!')
        return redirect('login')

    return render(request, 'registration/login.html')

def PROFILE(request):
    return render(request, 'registration/profile.html')

@login_required
def PROFILE_UPDATE(request):
    if request.method == "POST":
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user_id = request.user.id

        user = User.objects.get(id = user_id)

        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email

        if password != None and password != "":
            user.set_password(password)
        
        user.save()
        messages.success(request, 'Profile has been successfully updated')
        return redirect('profile')  # Redirect to the profile page after update

    return render(request, 'registration/profile_update.html')
   

