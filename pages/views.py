from django.shortcuts import render
from django.views.generic import TemplateView
from courses.Models.Category import Category
from courses.Models.CourseData import CourseData
from django.core.paginator import Paginator

def index(request):
    courseList = CourseData.objects.all().order_by('-id')
    paginator = Paginator(courseList,3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'categories':Category.objects.all().order_by('categoryName'),
        'page_obj':page_obj,
        }
    
   
    return render(request,'pagesAppFiles/index.html',context=context)

class AboutView(TemplateView):
    template_name = 'pagesAppFiles/about.html'