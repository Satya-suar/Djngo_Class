
from django.urls import path
from ShirtApp import views

urlpatterns = [
    path('shirt/',views.retrive_view),
    
]