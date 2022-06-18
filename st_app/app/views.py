from django.shortcuts import render
from django.contrib import messages
from newsapi import NewsApiClient

# Create your views here.
def home(request):
    newsapi = NewsApiClient(api_key ='f796cb1d025a48d5a894d5be063b1607')
    top = newsapi.get_top_headlines(sources ='techcrunch')
  
    l = top['articles']
    desc =[]
    news =[]
    img =[]
  
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news, desc, img)
    
    return render(request, "index.html", context ={"mylist":mylist})