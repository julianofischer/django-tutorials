from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == 'POST':
        # User clicked the button
        username = request.POST['username']
        password = request.POST['password1']

        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=username)
                return render(request, 'accounts/signup.html', {'error': 'Username has already been taken.'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=username, password=password)
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error': "Passwords doesn't match."})
    else:
        # User did not click the button
        return render(request, 'accounts/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error' : 'Username or password is incorrect.'})

    else:
        return render(request, 'accounts/login.html')

def logout(request):
    # TODO need to route to home page
    return render(request, 'accounts/signup.html')
