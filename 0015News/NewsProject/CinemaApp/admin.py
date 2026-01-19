from django.contrib import admin
from .models import Writer_Info, Actor_Actress_Info, Director_Info

# Register your models here.
admin.site.register(Writer_Info)
admin.site.register(Actor_Actress_Info) 
admin.site.register(Director_Info)
