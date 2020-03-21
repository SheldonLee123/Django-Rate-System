import json

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.urls import reverse
from rest_framework import viewsets
from .models import Teacher, Module, User_Rate, Taught_by
from .serializers import ModuleSerializer, TeacherSerializer


'''
code
200 normal
100 require login
101 use POST method
102 require correct input
'''

class ModuleView(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer


class TeacherView(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

#register
def Register(request):
    ret= {}
    if request.method == 'POST':
        data = json.loads(request.body)
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        # email = request.POST.get('email')
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        user = User.objects.filter(username=username)
        if user:     #username already register
            ret['msg'] = 'The user already exists, please choose a new username!'
            return JsonResponse(ret)
        em = User.objects.filter(email=email)
        if em:    #email already exists
            ret['msg'] = 'This email address is already registered, please use another email!'
            return JsonResponse(ret)
        new_user = User.objects.create_user(username=username, password=password, email=email)
        ret['msg'] = 'Create new user successfully!'
        return JsonResponse(ret)
    ret['code'] = 101
    ret['msg'] = 'Please use POST!'
    return JsonResponse(ret)

#login
def Login(request):
    ret = {}
    if request.method == 'POST':
        data = json.loads(request.body)
        # username = request.POST.get('username')
        # password = request.POST.get('password')
        username = data.get('username')
        password = data.get('password')
        user = auth.authenticate(username=username, password=password)
        if not user:
            ret['msg'] = 'Password or Username is incorrect!'
            # ret['username'] = username
            # ret['password'] = password
            return JsonResponse(ret)
        else:
            request.session["login_user"] = username
            ret['msg'] = 'Welcome ' + username + ', Login Success!'
            return JsonResponse(ret)
    ret['code'] = 100
    ret['msg'] = 'You have not log in, Please log in first!'
    return JsonResponse(ret)

def check_user(func):
    def inner(*args, **kwargs):
        # judge login
        username = args[0].session.get("login_user", "")
        if username == "":
            # redirect
            return redirect("/login/")
        return func(*args, **kwargs)
    return inner

@check_user
def Logout(request):
    ret = {"msg": "Logout successfully!"}
    return JsonResponse(ret)

@check_user
def View(request):
    ret = {}
    teachers = Teacher.objects.all()
    for teacher in teachers:
        taught_bys = Taught_by.objects.filter(teacher_id_id=teacher.id)
        overall = []
        for taught_by in taught_bys:
            rates = User_Rate.objects.filter(Taught_by_id_id=taught_by.id)
            for rate in rates:
                overall.append(rate.rate)
        rating = 0.0
        if overall:
            rating = sum(overall)/len(overall)
        # print(teacher.name)
        # print(int(rating))
        teacher_name = teacher.name + " (" + teacher.professor_id + ")"
        ret[teacher_name] = int(rating)
    # ret['msg'] = 'Nice!'
    ret['code'] = 200
    return JsonResponse(ret)

@check_user
def Average(request):
    ret = {}
    if request.method == 'POST':
        data = json.loads(request.body)
        professor_id = data.get('professor_id')
        module_code = data.get('module_code')
        teacher = Teacher.objects.filter(professor_id=professor_id).first()
        modules = Module.objects.filter(code=module_code)
        # print(modules)
        average = []
        if teacher and modules:
            for module in modules:
                taught_bys = Taught_by.objects.filter(teacher_id_id=teacher.id, module_id_id=module.id)
                # print(taught_bys)
                for taught_by in taught_bys:
                    rates = User_Rate.objects.filter(Taught_by_id_id=taught_by.id)
                    for rate in rates:
                        average.append(rate.rate)
            rating = 0.0
            if average:
                rating = sum(average) / len(average)
            ret[teacher.name] = int(rating)
            ret['module_name'] = str(modules[0])
            ret['code'] = 200
            return JsonResponse(ret)
        else:
            ret['code'] = 102
            ret['msg'] = 'Sorry, we do not find anything. Please input correct information!'
            return JsonResponse(ret)
    ret['code'] = 101
    ret['msg'] = 'Please use POST!'
    return JsonResponse(ret)

#Rate
@check_user
def Rate(request):
    ret = {}
    if request.method == 'POST':
        data = json.loads(request.body)
        professor_id = data.get('professor_id')
        module_code = data.get('module_code')
        year = data.get('year')
        semester = data.get('semester')
        rating = data.get('rating')
        print(data)
        # print(module_code, professor_id)
        # print(professor_id, module_code, year, semester, rating)
        if float(rating) >= 1.0 and float(rating) <= 5.0:
            module = Module.objects.filter(code=module_code, year=year, semester=semester).first()
            teacher = Teacher.objects.filter(professor_id=professor_id).first()
            taught_by = Taught_by.objects.filter(module_id=module.id, teacher_id=teacher.id).first()
            # print(module.id)
            # print(teacher.id)
            print(taught_by)
            if taught_by:
                new_rate = User_Rate.objects.create(Taught_by_id_id=taught_by.id, rate=rating)
                new_rate.save()
                ret['code'] = 200
                ret['msg'] = 'Rate successfully!'
                return JsonResponse(ret)
            else:
                ret['code'] = 102
                ret['msg'] = 'Sorry, we can not record your rate. Please input correct information!'
                return JsonResponse(ret)
        else:
            ret['msg'] = 'Please input correct rating!'
            return JsonResponse(ret)
    ret['code'] = 101
    ret['msg'] = 'Please use POST!'
    return JsonResponse(ret)

