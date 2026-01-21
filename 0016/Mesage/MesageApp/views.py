from django.shortcuts import render

# Create your views here.
def msg_view(request,name):
    d={'name':name}
    
    return render(request,'msg.html',d)

def add_view(request,a,b):
    add=a+b
    d={'add':add}
    return render(request,'add.html',d)