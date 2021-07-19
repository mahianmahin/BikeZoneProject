from django.shortcuts import render
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import redirect

def app_signup(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    else:
        if request.method == "POST":
            form = SignUpForm(request.POST)

            if form.is_valid():
                form.save()
        else:
            form = SignUpForm()
            
    context = {'form' : form}
    return render(request, 'auth_app/signup.html', context)


def app_login(request):
    if request.user.is_authenticated:
        messages.info(request, 'Already Logged In')
        return redirect('/dashboard/')
    else:
        invalid = False
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully!')
                return redirect('/dashboard/')

            else:
                invalid = True

    context = {'invalid' : invalid}
    return render(request, 'auth_app/login.html', context)

def app_logout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'Logged out')
        return redirect('/')
    else:
        return redirect('/')

