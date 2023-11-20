import requests
import json

api_key= " "#write your api key
category = input("What type of news are you interested in?(sports,technology,etc) \n ")
lines=input("How many headlinees do you want to read")


# url = f"https://newsapi.org/v2/everything?q={category}&from=2023-01-28&sortBy=publishedAt&apiKey={api_key}"
# r = requests.get(url)
# news = json.loads(r.text)
# print(news, type(news))
# for article in news["articles"]:
#   print(article["title"])
#   print(article["description"])
#   print("--------------------------------------")
  
def news():

    url = f"https://newsapi.org/v2/everything?q={category}&from=2023-01-28&sortBy=publishedAt&apiKey={api_key}"
    news =requests.get(url)
    news2 = json.loads(news.text)
    article = news["articles"]
    news_article = []
    for arti in article:
        news_article.append(arti["title"])
    for i in range(lines):
        print(news_article[i])
news()        
     