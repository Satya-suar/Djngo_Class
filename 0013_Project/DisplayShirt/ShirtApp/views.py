from django.shortcuts import render
from .models import Shirt

# Create your views here.
def retrive_view(request):
    shirts = Shirt.objects.all()
    d = {'shirts':shirts}
    return render(request, 'shirtapp/shirt.html', d)