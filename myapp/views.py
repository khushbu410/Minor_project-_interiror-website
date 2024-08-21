from django.shortcuts import render,redirect
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm
from .models import Booking


def index(request):
    return render(request, '../Templates/New_Templates/index.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Hi ,{username}')
            return redirect('myapp')
        else:
            # Invalid login
            return render(request, '../Templates/login.html', {'error': 'Invalid username or password'})
    return render(request, '../Templates/login.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.first_name = form.cleaned_data.get('fname')
            user.last_name = form.cleaned_data.get('lname')
            user.save()

            messages.success(request, 'Account created successfully. Please log in.')

            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, '../Templates/SignUp.html', {'error':form.errors})

def logout_view(request):
    logout(request)
    return redirect('myapp')

@login_required(login_url='/login/') 
def Book_view(request,service_name):
    if request.method == "POST":
        new_booking = Booking()
        new_booking.user = request.user
        new_booking.designer_name = request.POST.get('DesignerName')
        new_booking.date_time = request.POST.get('Date')
        new_booking.phone_number = request.POST.get('PhoneNumber')
        new_booking.location = request.POST.get('Location')
        new_booking.service_name = service_name
        new_booking.save()
      
        messages.success(request, 'Your booking has been successfully submitted!')
       
        return redirect('myapp')
    return render(request, '../Templates/Book.html', {'service_name': service_name})

def meet_designer(request):
    bookings = Booking.objects.filter(user=request.user) 
    return render(request,'../Templates/bookings.html',{'bookings': bookings})

def how_it_work(request):
    return render(request,'../Templates/New_Templates/How It works.html')  

def services(request):
    return render(request,'../Templates/New_Templates/service.html') 

def singleblog(request):
    return render(request,'../Templates/New_Templates/single.html') 

def contect(request):
    return render(request,'../Templates/New_Templates/contact.html')   
# Create your views here.
