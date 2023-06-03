from django.urls import path
from .views import Login
urlpatterns = [
    path('',Login,name='login')
]
