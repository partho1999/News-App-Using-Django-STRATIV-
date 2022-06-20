# # importing requests package
# import requests    
 
# def NewsFromSource(source):
     
#     # BBC news api
#     # following query parameters are used
#     # source, sortBy and apiKey
#     query_params = {
#       "source": source,
#       "sortBy": "top",
#       "apiKey": "f796cb1d025a48d5a894d5be063b1607"
#     }
#     main_url = " https://newsapi.org/v1/articles"
 
#     # fetching data in json format
#     res = requests.get(main_url, params=query_params)
#     open_bbc_page = res.json()
#     print(open_bbc_page)
#     return open_bbc_page
# #     # getting all articles in a string article
# #     article = open_bbc_page["articles"]
 
# #     # empty list which will
# #     # contain all trending news
# #     results = []
     
# #     for ar in article:
# #         results.append(ar["title"])
         
# #     for i in range(len(results)):
         
# #         # printing all trending news
# #         print(i + 1, results[i])
 
#  # Driver Code
# if __name__ == '__main__':
     
#     # function call
#     NewsFromSource("bbc-news")


# from newsapi import NewsApiClient

# # Init
# newsapi = NewsApiClient(api_key='f796cb1d025a48d5a894d5be063b1607')

# # /v2/top-headlines
# top_headlines = newsapi.get_top_headlines(q='bitcoin',
#                                          # sources='bbc-news,the-verge',
#                                           category='business',
#                                           language='en',
#                                           country='us')
# print(top_headlines)

import requests
# url = ('https://newsapi.org/v2/top-headlines?'
#        'country=us&'
#        'category=business&'
#        'apiKey=f796cb1d025a48d5a894d5be063b1607')
# response = requests.get(url)
# print response.json()
#####################################country######################################
# import requests
# API_KEY = 'd0b69496c18e463f888a273cb521ea9f'
# country = 'us'
# url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
# response = requests.get(url)
# data = response.json()
# articles = data['articles']
# print(articles)
###################################################################################
# from newsapi import NewsApiClient
# sources = 'bbc-news,the-verge'
# newsapi = NewsApiClient(api_key ='f796cb1d025a48d5a894d5be063b1607')
# top = newsapi.get_top_headlines(sources = sources)
  
# articles = top['articles']
# print(articles)

test_list = [1, None, 4, None, None, 5, 8, None]
  
# printing original list 
print ("The original list is : " + str(test_list))

res = []
for val in test_list:
    if val != None :
        res.append(val)
print ("List after removal of None values : " +  str(res))