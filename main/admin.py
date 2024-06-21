from django.contrib import admin
from .import models 


admin.site.register(models.User)
admin.site.register(models.Comment)
admin.site.register(models.Course)
admin.site.register(models.Teacher)
admin.site.register(models.Like)
admin.site.register(models.Lesson)
