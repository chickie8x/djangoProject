from concurrent.futures import ThreadPoolExecutor
from time import perf_counter

from django.http import JsonResponse
from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup
from demoFE.models import Article


# Create your views here.

def index(request):
    req = requests.get('https://tuoitre.vn')
    return render(request, 'demoFE/index.html', {'ctx': req.text})


def crawl(request):
    start_time = perf_counter()
    base_url = 'https://tuoitre.vn'
    if request.method == 'POST':
        links = request.POST['links']
        links_format = [base_url + item for item in links.split(',')]

        # internal function
        def crawl(url):
            req = requests.get(url)
            soup = BeautifulSoup(req.text, 'html.parser')
            title = soup.findAll('h1', attrs={'class': 'article-title'})[0].text
            desc = soup.findAll('h2', attrs={'class': 'sapo'})[0].text
            content = soup.findAll('div', attrs={'class': 'content fck'})[0]
            content_p = content.findAll('p', recursive=False)
            content_text = ''
            for p in content_p:
                content_text += p.text
            imgs = ''
            img_container = soup.findAll('div', attrs={'class': 'VCSortableInPreviewMode'})
            for item in img_container:
                try:
                    imgs += (item.img['data-original'])+','
                except:
                    pass
            obj = Article.objects.get_or_create(article_title=title, article_desc=desc, article_content=content_text , imgs=imgs)
            obj.save()

        with ThreadPoolExecutor() as executor:
            executor.map(crawl, links_format)

        stop_time = perf_counter()
        print('duration: ', stop_time - start_time)
        return JsonResponse({'mes': 'success'}, status=200)
    else:
        return JsonResponse({'mes': 'failed'}, status=200)


def article(request,path):
    if path[0:5] != 'https':
        return redirect('https://tuoitre.vn/'+path)
    else:
        return redirect(path)