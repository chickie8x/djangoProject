from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crawl/', views.crawl, name='crawl'),
    path('<str:path>/',views.article,name='article')
]