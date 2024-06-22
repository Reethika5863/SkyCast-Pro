from django.shortcuts import render
from django.http import HttpResponse
from .models import contact

def index(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def cont(request):
    return render(request,"contact.html")

def docontact(request):
    mobile=request.GET['mobile']
    email=request.GET['email']
    address=request.GET['address']
    c=contact()
    c.Mobile=mobile
    c.email=email
    c.address=address
    c.save()
    return render(request,"contact.html",{"msg":"Contact successfull"})
