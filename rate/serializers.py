from rest_framework import serializers
from .models import Module, Teacher, Taught_by
from django.db import models

class ModuleSerializer(serializers.ModelSerializer):
    taught_by = serializers.SerializerMethodField()
    class Meta:
        model = Module
        fields = ('id', 'code', 'name', 'year', 'semester', 'taught_by')

    def get_taught_by(self, obj):
        taught = obj.taught_by_set.all()
        t = Taught_bySerializer(taught, many=True)
        return t.data

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'name')

class Taught_bySerializer(serializers.ModelSerializer):
    teacher_id = serializers.IntegerField(source='teacher_id.id')
    teacher_name = serializers.CharField(source='teacher_id.name')
    professor_id = serializers.CharField(source='teacher_id.professor_id')
    class Meta:
        model = Taught_by
        fields = ('teacher_id', 'teacher_name', 'professor_id')
