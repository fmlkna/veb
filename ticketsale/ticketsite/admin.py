from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.register(User, UserAdmin)
admin.site.register(City)
admin.site.register(Place)
admin.site.register(Event)
admin.site.register(Ticket)
admin.site.register(Order)
