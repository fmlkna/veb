from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .models import Event, City, Order

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

def login_view(request):
    if request.method == 'POST':
        pass
    return render(request, 'ticketsite/login.html')

def logout_view(request):
    logout(request)
    return redirect('index')