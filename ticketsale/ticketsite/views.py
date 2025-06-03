from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .models import Event, City, Order, User

@csrf_protect
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username') 
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            try:
                User.objects.get(username=username)
                messages.error(request, 'Неверный пароль')
            except User.DoesNotExist:
                messages.error(request, 'Пользователь с таким логином не найден')
    
    return render(request, 'ticketsite/login.html')

def user_register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Пользователь с таким логином уже существует!')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Пользователь с таким email уже существует!')
        else:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            login(request, user)
            return redirect('profile')
    
    return render(request, 'ticketsite/register.html')

def index(request):
    cities = City.objects.all()
    return render(request, 'ticketsite/index.html', {'cities': cities})

def events(request):
    city_id = request.GET.get('city')
    events = Event.objects.all()
    if city_id:
        events = events.filter(place__city_id=city_id)
    return render(request, 'ticketsite/events.html', {'events': events})

def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    orders = Order.objects.filter(user=request.user)
    return render(request, 'ticketsite/profile.html', {'orders': orders})

def contacts(request):
    return render(request, 'ticketsite/contacts.html')

def logout_view(request):
    logout(request)
    return redirect('index')

def event_detail(request, event_id):
    event = Event.objects.get(id=event_id)
    return render(request, 'ticketsite/event_detail.html', {'event': event})

