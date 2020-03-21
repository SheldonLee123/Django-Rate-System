from django.contrib import admin
from .models import Module, Teacher, User_Rate, Taught_by

class ModuleAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'year', 'semester')

admin.site.register(Module, ModuleAdmin)
admin.site.register(Teacher)
admin.site.register(User_Rate)
admin.site.register(Taught_by)