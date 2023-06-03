from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm,RegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from courses.Models.Course import Course
from django.contrib.auth.models import User
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

@login_required(login_url='login')
def Dashboard(request):
    current_user = request.user
    courses = current_user.courses_joined.all()
    if len(courses) == 0:
        messages.info(request,'Kayıtlı Olduğunuz Kurs Bulunmamaktadır!')
    data = {
        'courses':courses
    }
    return render(request,'accountsAppFiles/dashboard.html',context=data)

def enrolTheCourse(request):
    user = User.objects.get(id = request.POST['user_id'])
    course = Course.objects.get(id = request.POST['courseId'])
    
    course.students.add(user)
    
    return redirect('dashboard')

def releaseTheCourse(request):
    user = User.objects.get(id = request.POST['user_id'])
    course = Course.objects.get(id = request.POST['courseId'])
    
    course.students.remove(user)
    
    return redirect('dashboard')