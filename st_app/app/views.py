from django.shortcuts import render
from django.contrib import messages
from newsapi import NewsApiClient
import requests

API_KEY = 'd0b69496c18e463f888a273cb521ea9f'
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

def Newsfeed(request):
    if request.method == "GET":
        # country = request.GET.get('country')
        # category = request.GET.get('category')
        cou = request.GET.get('dropdown')
        cat = request.GET.get('dropdown1')
        print(cou, cat)

        url = f'https://newsapi.org/v2/top-headlines?country={cou}&category={cat}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']  
    
    print("im here")
    url = f'https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']

    # if country:
    #     url = f'https://newsapi.org/v2/top-headlines?country={cou}&category={cat}apiKey={API_KEY}'
    #     response = requests.get(url)
    #     data = response.json()
    #     articles = data['articles']
    # else:
    #     url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
    #     response = requests.get(url)
    #     data = response.json()
    #     articles = data['articles']
    #import requests
    # url = ('https://newsapi.org/v2/top-headlines?'
    #     'country={country}&'
    #     #'category={category}&'
    #     'apiKey=f796cb1d025a48d5a894d5be063b1607')
    # response = requests.get(url)
    # data = response.json()
    # articles = data['articles']



    context = {
        'articles' : articles
    }

    return render(request, 'setting.html', context)
