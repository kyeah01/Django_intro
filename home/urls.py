from django.urls import path
from . import views
# 자기껄로부터 불러오니까 .임

urlpatterns = [
    path('static_example/', views.static_example, name='static_example'),
    path('template_example', views.template_example, name='template_example'),
    path('user_create/', views.user_create, name='user_create'),
    path('user_new/', views.user_new, name='user_new'),
    path('pong/', views.pong, name='pong'),
    path('ping/', views.ping, name='ping'),
    path('cube/<int:num>/', views.cube, name='cube'),
    path('hello/<name>/', views.hello, name='hello'),
    path('dinner/', views.dinner, name='diner_menu'),
    path('index/', views.index, name='index'),
]