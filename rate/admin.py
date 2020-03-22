from django.contrib import admin
from .models import Module, Teacher, User_Rate, Taught_by

class ModuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'code', 'name', 'year', 'semester')

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'professor_id')

class Taught_byAdmin(admin.ModelAdmin):
    list_display = ('id', 'teacher_id', 'module_id')

admin.site.register(Module, ModuleAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(User_Rate)
admin.site.register(Taught_by, Taught_byAdmin)