from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm,RegisterForm
from django.contrib import messages
# Create your views here.


def Login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                
                user = authenticate(request,username=username,password=password)
                if user is not None:
                    if user.is_active:
                        login(request,user)
                        return redirect('courses')
                    else:
                        messages.info(request,'Hesap aktif değil!')
                else:
                    messages.info(request,'Kullanıcı Adı veya Parola Hatalı')
                    
        else:
            form = LoginForm()
        return render(request,'accountsAppFiles/login.html',context={
            'form':form
        })

def Register(request):
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Hesabınız oluşturuldu')
            return redirect('login')
    else:
        form = RegisterForm()
    
    return render(request,'accountsAppFiles/register.html',context={
        'form':form
    })
    
def Logout(request):
    logout(request)
    return render(request,'accountsAppFiles/logout.html')