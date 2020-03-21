from django.urls import path, include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('module', views.ModuleView)
# router.register('teacher', views.TeacherView)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', views.Login),
    path('register/', views.Register),
    path('logout/', views.Logout),
    path('rate/', views.Rate),
    path('view/', views.View),
    path('average/', views.Average),
]

