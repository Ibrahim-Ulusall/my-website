from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="home"),
    path('about/',views.AboutView.as_view(),name='about')
]
