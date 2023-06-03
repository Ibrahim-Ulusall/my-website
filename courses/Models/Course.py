from django.db import models
from django.utils.text import slugify
from .CourseName import CourseName
from .Category import Category
from .Teachers import Teacher


class Course(models.Model):
    title = models.CharField(max_length=50)
    name = models.ForeignKey(CourseName,on_delete=models.CASCADE)
    category = models.ManyToManyField(Category,blank=True,null=True)
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
