from django.http import JsonResponse
from django.shortcuts import render
import requests
import json


# Create your views here.

def index(request):
    req = requests.get('https://tuoitre.vn')
    return render(request, 'demoFE/index.html', {'ctx': req.text})


def crawl(request):
    base_url = 'https://tuoitre.vn'
    if request.method == 'POST':
        links = request.POST['links']
        links_format = [ base_url + item for item in links.split(',')]
        print(links_format)


    return JsonResponse ({'mes': 'success'}, status=200)
