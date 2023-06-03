from django.db import models
from django.utils.text import slugify
class Teacher(models.Model):
    
    TeacherName = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    Description = models.TextField()
    image = models.ImageField(upload_to='teacher/%Y%m/%D',null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True,editable=False)

    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.TeacherName) 
        super().save(*args,**kwargs)   
    
    def __str__(self) -> str:
        return self.TeacherName.capitalize()