from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import register  # Replace with your actual model name

admin.site.register(register)