from django.urls import path
from .views import Login,Register,Logout,Dashboard,enrolTheCourse,releaseTheCourse
urlpatterns = [
    path('login',Login,name='login'),
    path('register',Register,name='register'),
    path('logout',Logout,name='logout'),
    path('dashboard',Dashboard,name='dashboard'),
    path('enrolTheCourse',enrolTheCourse,name='enrolTheCourse'),
    path('releaseTheCourse',releaseTheCourse,name='releaseTheCourse'),
]
