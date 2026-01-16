from django.urls import path
from ModelApp import views

urlpatterns = [
    
    path('data/',views.Student_View)
]