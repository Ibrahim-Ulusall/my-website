from django.db import models
from django.utils.text import slugify

class CourseName(models.Model):
    courseName = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True,editable=False)
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.courseName)
        super().save(*args,**kwargs)
        
    def __str__(self) -> str:
        return self.courseName.capitalize()