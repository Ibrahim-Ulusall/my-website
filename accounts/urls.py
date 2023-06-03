from django.urls import path
from .views import Login,Register,Logout
urlpatterns = [
    path('login',Login,name='login'),
    path('register',Register,name='register'),
    path('logout',Logout,name='logout'),
]
