from django.shortcuts import render, HttpResponse
from pprint import pprint
import random

# Create your views here.
def index(request):
    # print(request)
    # print(type(request))
    # pprint(request.META)
    return HttpResponse('Welcome to Django!')
    
def dinner(request):
    menu = ['슈프림치킨', '철판볶음밥', '연어', '소고기', '장조림']
    pick = random.choice(menu)
    # return HttpResponse(random.choice(menu))
    return render(request, 'dinner.html', {'menus' : menu, 'pick' : pick})
    
def hello(request, name):
    return render(request, 'hello.html', {'name': name })
    
def cube(request, num):
    cube = num **3
    return render(request, 'cube.html', {'num': num, 'cube':cube })
    
def ping(request):
    return render(request, 'ping.html')
    
def pong(request):
    print(request.GET)
    data = request.GET.get('data')
    return render(request, 'pong.html', {'data':data })

def user_new(request):
    return render(request, 'user_new.html')

def user_create(request):
    nickname = request.POST.get('nickname')
    password = request.POST.get('password')
    return render(request, 'user_create.html', {'nickname':nickname, 'password':password})