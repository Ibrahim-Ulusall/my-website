from django.db import models
from django.utils.text import slugify
from .CourseName import CourseName
from .Category import Category
from .Teachers import Teacher
from django.contrib.auth.models import User


class Course(models.Model):
    title = models.CharField(max_length=50,help_text="Course Adı ile aynı olsun!")
    name = models.ForeignKey(CourseName,on_delete=models.CASCADE)
    category = models.ManyToManyField(Category,blank=True,null=True)
    teachers = models.ForeignKey(Teacher,on_delete=models.CASCADE,blank=True,null=True)
    students = models.ManyToManyField(User,null=True,blank=True,related_name='courses_joined')
    description = models.TextField()
    image = models.ImageField(upload_to='courses/%Y-%m/%d/',blank=True,null=True)
    isActive = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True,editable=False)
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)
    
    def __str__(self) -> str:
        return self.title.capitalize()
