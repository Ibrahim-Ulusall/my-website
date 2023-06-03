from django.urls import path
from .views import course, course_details,course_data_details,\
                    categoryList,allTeachers,teacherDetails
urlpatterns = [
    path('',course,name='courses'),
    path('<slug:courseSlug>/<int:id>',course_details,name='course-details'),
    path('<int:id>',course_data_details,name = 'course-data-details'),
    path('category/<slug:categories_slug>',categoryList,name = 'categories'),
    path('teachers',allTeachers,name='teachers'),
    path('teacher/<slug:teacherSlug>',teacherDetails,name='teacherDetails'),
]
