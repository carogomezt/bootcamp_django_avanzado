from django.contrib import admin

from .models import Client, SportClass, Booking

# Register your models here.
admin.site.register(Client)
admin.site.register(SportClass)
admin.site.register(Booking)
