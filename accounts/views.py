from django.shortcuts import render

# Create your views here.


def Login(request):
    return render(request,'accountsAppFiles/login.html')

def Register(request):
    return render(request,'accountsAppFiles/register.html')