from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),    
    path('bye/', views.bye, name='bye'),    
    path('graduation/', views.graduation, name='graduation'),
    path('imagepick/', views.imagepick, name='imagepick'),
    path('today/', views.today),
    path('ascii_new/', views.ascii_new),
    path('ascii_make/', views.ascii_make),
    path('original/', views.original),
    path('translated/', views.papago),
]