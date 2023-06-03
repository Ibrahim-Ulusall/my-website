from django.contrib import admin
from .Models.Category import Category
from .Models.Teachers import Teacher
from .Models.Course import Course
from .Models.CourseData import CourseData
from .Models.CourseName import CourseName

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('categoryName','slug','date')
    list_filter = ('date',)
    
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('TeacherName','slug','date')
    list_filter = ('TeacherName','date',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
   list_display = ('title','slug','date')
   list_filter = ('slug','date')

@admin.register(CourseData)
class CourseDataAdmin(admin.ModelAdmin):
    list_display = ('name','slug','date')
    list_filter = ('name','date',)

@admin.register(CourseName)
class CourseNameAdmin(admin.ModelAdmin):
    list_display = ('courseName','slug','date')
    list_filter = ('date',)
