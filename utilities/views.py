from django.shortcuts import render
from datetime import datetime
import requests, json, os

# Create your views here.
def index(request):
    return render(request, 'utilities/index.html')
    
def bye(request):
    time = datetime(2019, 2, 28, 18) - datetime.now()
    return render(request, 'utilities/bye.html', {'time':time})
    
def graduation(request):
    time = datetime(2019, 5, 28) - datetime.now()
    return render(request, 'utilities/graduation.html', {'time':time})
    
def imagepick(request):
    return render(request, 'utilities/imagepick.html')
    
def today(request):
    time = datetime.now()
    token = os.getenv('W_TOKEN')
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q=Seoul,kr&lang=kr&APPID={token}").json()
    weather = response.get('weather')[0].get('description')
    temp = round(response.get('main').get('temp') - 273.15, 0)
    return render(request, 'utilities/today.html', {'time': time, 'weather':weather, 'temp': temp})
    
    
def ascii_new(request):
    return render(request, 'utilities/ascii_new.html')
    
def ascii_make(request):
    sentence = request.GET.get('text')
    how = request.GET.get('how')
    result = requests.get(f'http://artii.herokuapp.com/make?text={sentence}&font={how}').text
    return render(request, 'utilities/ascii_make.html', {'result' : result})

def original(request):
    return render(request, 'utilities/original.html')

def papago(request):
    text = request.GET.get('text')
    headers = {'X-Naver-Client-Id' : os.getenv('NAVER_CLIENT_ID'),
                'X-Naver-Client-Secret' : os.getenv('NAVER_CLIENT_SECRET')}
    data = {
        "source": "ko",
        "target": "en",
        "text": text
        }
    papago_url = f'https://openapi.naver.com/v1/papago/n2mt'
    req = requests.post(papago_url, headers=headers, data=data).json().get('message').get('result').get('translatedText')
    return render(request, 'utilities/papago.html', {'req':req})