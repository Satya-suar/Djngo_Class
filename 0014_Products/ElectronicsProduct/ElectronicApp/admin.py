from django.contrib import admin
from .models import Electronics

# Register your models here.

# admin.site.register(Electronics)

@admin.register(Electronics)
class ElectronicsAdmin(admin.ModelAdmin):
    list_display = ['id','PName','Brand','Price']
