import datetime

from django.db import models

class Module(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    semester = models.IntegerField()

    class Meta:
        unique_together = ('code', 'year', 'semester')

    def __str__(self):
        res = str(self.code)+"("+str(self.year)+","+str(self.semester)+")"
        return res

class Teacher(models.Model):
    name = models.CharField(max_length=50, unique=True)
    professor_id = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Taught_by(models.Model):
    teacher_id = models.ForeignKey("Teacher", on_delete=models.CASCADE)
    module_id = models.ForeignKey("Module", on_delete=models.CASCADE)

    class Meta:
        unique_together = ('teacher_id', 'module_id',)

class User_Rate(models.Model):
    Taught_by_id = models.ForeignKey("Taught_by", on_delete=models.CASCADE)
    rate = models.IntegerField()        # 1-5
    data_publish = models.DateTimeField(default=datetime.datetime.now)

