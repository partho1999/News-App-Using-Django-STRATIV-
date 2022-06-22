from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import numpy as np
from newsapi import NewsApiClient
import requests
import os.path
# from os import path
import pandas as pd
import os
from math import nan, isnan

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
    filename ="media/"+username+".csv"
    if os.path.exists(filename) :
        print("file exists")
        path = "media/"
        dir_list = os.listdir(path)
        filtered_lst=[]
        for element in dir_list:
            if username in element:     
                filtered_lst.append(element)
        print(filtered_lst[0]) 

        df2=pd.read_csv(path+filtered_lst[0])
        frames = [df2, df]
        result = pd.concat(frames)
        result.to_csv('media/'+username +'.csv', index=False, header=True)
    else:
        print ("file couldn't found")
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
        #pdf['Searched_country']= pdf['Searched_country'].fillna(0)
        print(pdf)
        #print(type(pdf["Searched_country"]))
        lst = pdf['Searched_country'].to_list()
        
        
        cntry =pdf["Searched_country"].iloc[-1]
        
        print("cntry value:",cntry)
        
        result =[]
        for val in lst:
            print(type(val))
            if type(val) == str:
                result.append(val)
        print("result",result)
        
        if result:
            print("not null")
            articles=[]
            for item in result:
                url = f'https://newsapi.org/v2/top-headlines?country={item}&apiKey={API_KEY}'
                response = requests.get(url)
                data = response.json()
                article = data['articles']
                for i in article:
                    articles.append(i)
        else:
            print("null")
            articles=[]
            for item in categories:
                    url = f'https://newsapi.org/v2/top-headlines?category={item}&apiKey={API_KEY}'
                    response = requests.get(url)
                    data = response.json()
                    article = data['articles']
                    for i in article:
                            articles.append(i)

        # if lst != 0:
        #     res=[]
        #     print("lst is not none")
        #     for val in lst:
        #         if val != 0:
        #             res.append(val)
        #     articles=[]
        #     for item in res:
        #         url = f'https://newsapi.org/v2/top-headlines?country={cntry}&apiKey={API_KEY}'
        #         response = requests.get(url)
        #         data = response.json()
        #         article = data['articles']
        #         for i in article:
        #             articles.append(i)
            
            
        # else:
        #     print("im in else")
        #     articles=[]
        #     for item in categories:
        #         url = f'https://newsapi.org/v2/top-headlines?category={item}&apiKey={API_KEY}'
        #         response = requests.get(url)
        #         data = response.json()
        #         article = data['articles']
        #         for i in article:
        #             articles.append(i)
   
    
        


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
    categories = ['business', 'entertainment',  'health', 'science', 'sports', 'technology']
    option_1 = request.GET.get('task_1')
    option_2 = request.GET.get('task_2')
    option_3 = request.GET.get('task_3')
    option_4 = request.GET.get('task_4')
    option_5 = request.GET.get('task_5')
    option_6 = request.GET.get('task_6')
    option_7 = request.GET.get('task_7')
    option_8 = request.GET.get('task_8')
    option_9 = request.GET.get('task_9')
    option_10 = request.GET.get('task_10')
    option_11 = request.GET.get('task_11')
    option_12 = request.GET.get('task_12')
    option_13 = request.GET.get('task_13')
    option_14 = request.GET.get('task_14')
    option_15 = request.GET.get('task_15')
    option_16 = request.GET.get('task_16')
    option_17 = request.GET.get('task_17')
    option_18 = request.GET.get('task_18')
    option_19 = request.GET.get('task_19')
    option_20 = request.GET.get('task_20')
    option_21 = request.GET.get('task_21')
    option_22 = request.GET.get('task_22')
    option_23 = request.GET.get('task_23')
    option_24 = request.GET.get('task_24')
    option_25 = request.GET.get('task_25')
    option_26 = request.GET.get('task_26')
    option_27 = request.GET.get('task_27')
    option_28 = request.GET.get('task_28')
    option_29 = request.GET.get('task_29')
    option_30 = request.GET.get('task_30')
    option_31 = request.GET.get('task_31')
    option_32 = request.GET.get('task_32')
    option_33 = request.GET.get('task_33')
    option_34 = request.GET.get('task_34')
    option_35 = request.GET.get('task_35')
    option_36 = request.GET.get('task_36')
    option_37 = request.GET.get('task_37')
    option_38 = request.GET.get('task_38')
    option_39 = request.GET.get('task_39')
    option_40 = request.GET.get('task_40')
    option_41 = request.GET.get('task_41')
    option_42 = request.GET.get('task_42')
    option_43 = request.GET.get('task_43')
    option_44 = request.GET.get('task_44')
    option_45 = request.GET.get('task_45')
    option_46 = request.GET.get('task_46')
    option_47 = request.GET.get('task_47')
    option_48 = request.GET.get('task_48')
    option_49 = request.GET.get('task_49')
    option_50 = request.GET.get('task_50')
    option_51 = request.GET.get('task_51')
    option_52 = request.GET.get('task_52')
    
    print("option_1: ", option_1)
    print("option_2: ", option_2)
    print("option_3: ", option_3)
    print("option_4: ", option_4)
    option_lst =[option_1, option_2, option_3, option_4, option_5,option_6,option_6,option_7,option_8, option_9,option_10,option_11,option_12,option_13, option_14,option_15,option_16,option_17,option_18, option_19,option_20,option_21,option_22,option_23, option_24,option_25,option_26,option_27,option_28, option_29,option_30,option_31,option_32,option_33, option_34,option_35,option_36,option_37,option_38, option_39,option_40,option_41,option_42,option_43, option_44,option_45,option_46,option_47,option_48, option_49,option_50,option_51,option_52]
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
    elif option_lst != [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]:
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
        #pdf['Searched_country']= pdf['Searched_country'].fillna(0)
        print(pdf)
        #print(type(pdf["Searched_country"]))
        lst = pdf['Searched_country'].to_list()
        
        cntry =pdf["Searched_country"].iloc[-1]
        
        print("cntry value:",cntry)
        
        result =[]
        for val in lst:
            print(type(val))
            if type(val) == str:
                result.append(val)
        print(result)
        if result:
            print("not null")
            articles=[]
            for item in result:
                url = f'https://newsapi.org/v2/top-headlines?country={item}&apiKey={API_KEY}'
                response = requests.get(url)
                data = response.json()
                article = data['articles']
                for i in article:
                    articles.append(i)
        else:
            print("null")
            articles=[]
            for item in categories:
                    url = f'https://newsapi.org/v2/top-headlines?category={item}&apiKey={API_KEY}'
                    response = requests.get(url)
                    data = response.json()
                    article = data['articles']
                    for i in article:
                            articles.append(i)

   
    
        


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