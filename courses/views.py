from django.shortcuts import render
from courses.Models.CourseData import CourseData
from courses.Models.Course import Course
from courses.Models.Category import Category
from courses.Models.Teachers import Teacher
from django.core.paginator import Paginator
from django.contrib import messages

def course(request):
    data = Course.objects.all().order_by('-id')
    paginator = Paginator(data,4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    return render(request,'courseAppFiles/courses.html',context={
        'courses':data,
        'categories':Category.objects.all().order_by('categoryName'),
        'page_obj':page_obj
    })

def course_details(request,courseSlug,id):
    
    data = Course.objects.get(slug=courseSlug,id=id)
    c = CourseData.objects.all().filter(name__slug = courseSlug)
    student = Course.objects.get(id = id)
    return render(request,'courseAppFiles/course_details.html',context={
        'data':data,
        'all_data':c,
        'isEnroll': student.is_student_registered(request.user)
    })

def course_data_details(request,id):
    
    context = CourseData.objects.get(id = id)
    
    return render(request,'courseAppFiles/course_data_details.html',context= {
        'data':context
    })


def categoryList(request,categories_slug):
    courses = Course.objects.all().filter(category__slug__iexact = categories_slug)
    if len(courses) == 0:
        messages.info(request,'Kategori Boş')
    return render(request,'courseAppFiles/courses.html',context={
        'courses':courses,
        'categories':Category.objects.all().order_by('categoryName'),
    })

def allTeachers(request):
    teachers = Teacher.objects.all()
    if len(teachers) == 0:
        messages.info(request,'Sisteme Kayıtlı Eğitmen Bulunmamaktadır!')
        
    return render(request,'courseAppFiles/teachers.html',context={
        'all_teacher': teachers
    })