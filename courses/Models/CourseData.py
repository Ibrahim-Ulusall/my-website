from django.db import models
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField
from .CourseName import CourseName

class CourseData(models.Model):
    
    name = models.ForeignKey(CourseName,on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = RichTextUploadingField()
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True,editable=False)
    isShowhome = models.BooleanField(blank=True,null=True)
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)
        
    def __str__(self) -> str:
        return self.name.courseName.capitalize()