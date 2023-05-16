from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from . models import Reservations

# Create your views here.


def register(request):
    user = User.objects.values('is_staff')
    val = ''
    for i in user:
        val = i['is_staff']
    if val == False:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password']
            password2 = request.POST['password_confirm']

            if password1 == password2:
                user = User.objects.create_user(
                    username=username, email=email, password=password1)
                user.save()
                user = auth.authenticate(username=username, password=password1)
                auth.login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Password Not the same')
                return redirect('register')
        else:
            return render(request, 'register.html')


def home(request):
    return render(request, 'home.html')


def guidelines(request):
    return render(request, 'guidelines.html')


def book(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        date = request.POST['date']

        p = Reservations(first_name=fname,  last_name=lname,  email=email,
                         reserved_date=date)
        p.save()
        return redirect('home')
    else:
        return render(request, 'book.html')


def bookings(request):
    rows = Reservations.objects.all()
    context = {
        'rows': rows
    }
    return render(request, 'bookings.html', context)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('home')


def logout(request):
    auth.logout(request)
    return redirect('home')


def base(request):
    return redirect('register')
