from django.shortcuts import render,HttpResponse
from .models import StudentData

# Create your views here.
def Student_View(request):
    records=StudentData.objects.all()
    return HttpResponse(records)
