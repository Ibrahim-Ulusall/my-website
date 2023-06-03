from django.shortcuts import render
from courses.Models.CourseData import CourseData
from courses.Models.Course import Course
from courses.Models.Category import Category
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
    return render(request,'courseAppFiles/course_details.html',context={
        'data':data,
        'all_data':c
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
    
    
    
    
    
    
    
"""

<div class="row my-5">
    <p>Sayfa : {{ page_obj.number }}/{{ page_obj.paginator.num_pages }}</p>
    <div class="col-md-4 offset-md-4">
        <nav aria-label="Page navigation example">
            <ul class="pagination">
                {% if page_obj.has_previous %}
                    <li class="page-item"><a class="page-link" href="?page={{ page_obj.previous_page_number }}">Geri</a></li>
                {% endif %}
                {% if page_obj.paginator.num_pages >= 3 %}
                    <li class="page-item"><a href="?page=1" class="page-link">1</a></li>
                    <li class="page-item"><a class="page-link" href="?page=2">2</a></li>
                    <li class="page-item"><a class="page-link" href="?page=3">3</a></li>
                {% endif %}
                {% if page_obj.has_next %}
                    <li class="page-item"><a class="page-link" href="?page={{ page_obj.next_page_number }}">İleri</a></li>
                {% endif %}
            </ul>
        </nav>
    </div>
</div>


"""