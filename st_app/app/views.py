from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import numpy as np
from newsapi import NewsApiClient
import requests
import pandas as pd
import os
API_KEY = 'f9ffadbb22b046e6b7634587e13969cc'

# Create your views here.
def home(request):
   
    
    return render(request, 'index.html')

@login_required
def Newsfeed(request):
    
    country = request.GET.get('country')
    category =request.GET.get('category')
    source = request.GET.get('source')
    username = request.user.username
    categories = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']
    print(category)

    countrylst =[country]
    sourcelst =[source]

    df = pd.DataFrame(
    {
     'Searched_country': countrylst,
     'Searched_source': sourcelst
    })
    df.to_csv('media/'+username +'.csv', index=False, header=True)
    url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']

            
    if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    elif source is not None:
        newsapi = NewsApiClient(api_key ='f9ffadbb22b046e6b7634587e13969cc')
        top = newsapi.get_top_headlines(sources = str(source))
        articles = top['articles']
    elif category is not None:
        
        print("i'm in the else")
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    else:
        path = "media/"
        dir_list = os.listdir(path)
        filtered_lst=[]
        for element in dir_list:
            if username in element:     
                filtered_lst.append(element)
        print(filtered_lst[0]) 

        pdf=pd.read_csv(path+filtered_lst[0])
        print(pdf)
        print(pdf["Searched_country"].values[0])
        cntry = pdf["Searched_country"].values[0]

        if cntry is None:
            url = f'https://newsapi.org/v2/top-headlines?country={cntry}&apiKey={API_KEY}'
            response = requests.get(url)
            data = response.json()
            articles = data['articles']
            
        else:
            for item in categories:
                url = f'https://newsapi.org/v2/top-headlines?category={item}&apiKey={API_KEY}'
                response = requests.get(url)
                data = response.json()
                articles = data['articles']
   
    
        


    context = {
        'articles' : articles
    }
    
    return render(request, "newsfeed.html", context)

@login_required
def Settings(request):
    category =request.GET.get('category')
    keyword = request.GET.get('keyword')
    print(keyword)
    username = request.user.username
    categories = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']
    option_1 = request.GET.get('task_1')
    option_2 = request.GET.get('task_2')
    option_3 = request.GET.get('task_3')
    option_4 = request.GET.get('task_4')
    print("option_1: ", option_1)
    print("option_2: ", option_2)
    print("option_3: ", option_3)
    print("option_4: ", option_4)
    option_lst = [option_1, option_2, option_3, option_4]
    print(option_lst)
    check_1 = request.GET.get('checkbox_1')
    check_2 = request.GET.get('checkbox_2')
    check_3 = request.GET.get('checkbox_3')
    check_4 = request.GET.get('checkbox_4')
    check_5 = request.GET.get('checkbox_5')
    check_6 = request.GET.get('checkbox_6')
    print("check_1: ", check_1)
    print("check_2: ", check_2)
    print("check_3: ", check_3)
    print("check_4: ", check_4)
    print("check_3: ", check_5)
    print("check_4: ", check_6)
    check_lst = [check_1, check_2, check_3, check_4, check_5, check_6]
    print(check_lst)
    API_KEY = 'f9ffadbb22b046e6b7634587e13969cc'
    
    # df = pd.DataFrame(
    # {
    #     'Searched_country': countrylst,
    #     'Searched_source': sourcelst
    # })
    # df.to_csv('media/'+username +'.csv', index=False, header=True)
    url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    articles = data['articles']

            
    if check_lst != [None, None, None, None, None, None]:
        res = []
        for val in check_lst:
            if val != None :
                res.append(val)
        articles= []
        for item in res:
                print(item)
                newsapi = NewsApiClient(api_key ='f9ffadbb22b046e6b7634587e13969cc')
                top = newsapi.get_top_headlines(sources = str(item))
                article= top['articles']
                for i in article:
                    articles.append(i)
    elif option_lst != [None, None, None, None]:
        res = []
        for val in option_lst:
            if val != None :
                res.append(val)
        articles= []
        for item in res:
            print(item)
            print("item are printed.......................")
            API_KEY = 'f9ffadbb22b046e6b7634587e13969cc'
            url = f'https://newsapi.org/v2/top-headlines?country={item}&apiKey={API_KEY}'
            response = requests.get(url)
            data = response.json()
            article = data['articles'] 
            for i in article:
                articles.append(i)    
    elif keyword != None:
        x = keyword.split(',')
        articles = []
        for item in x:
                newsapi = NewsApiClient(api_key ='f9ffadbb22b046e6b7634587e13969cc')
                top = newsapi.get_top_headlines(q=str(item))
                article= top['articles']
                for i in article:
                    articles.append(i)   
    elif category is not None:
        
        print("i'm in the else")
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
    else:
        path = "media/"
        dir_list = os.listdir(path)
        filtered_lst=[]
        for element in dir_list:
            if username in element:     
                filtered_lst.append(element)
        print(filtered_lst[0]) 

        pdf=pd.read_csv(path+filtered_lst[0])
        print(pdf)
        print(pdf["Searched_country"].values[0])
        cntry = pdf["Searched_country"].values[0]

        if cntry is None:
            url = f'https://newsapi.org/v2/top-headlines?country={cntry}&apiKey={API_KEY}'
            response = requests.get(url)
            data = response.json()
            articles = data['articles']
            
        else:
            for item in categories:
                url = f'https://newsapi.org/v2/top-headlines?category={item}&apiKey={API_KEY}'
                response = requests.get(url)
                data = response.json()
                articles = data['articles']
   
    
        


    context = {
        'articles' : articles
    }

    return render(request, 'setting.html',context)

def test(request):
    option_1 = request.GET.get('task_1')
    option_2 = request.GET.get('task_2')
    option_3 = request.GET.get('task_3')
    option_4 = request.GET.get('task_4')
    print("option_1: ", option_1)
    print("option_2: ", option_2)
    print("option_3: ", option_3)
    print("option_4: ", option_4)
    return render(request, 'country_dropdown.html')