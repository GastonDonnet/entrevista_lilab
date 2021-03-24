from django.contrib import admin
from .models import Client, Credit

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass

@admin.register(Credit)
class CreditAdmin(admin.ModelAdmin):
    pass