from django.shortcuts import render
import requests

# Create your views here.
def index(request):
    req = requests.get('https://tuoitre.vn')
    return render(request, 'demoFE/index.html',{'ctx': req.text})