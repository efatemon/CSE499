from bs4 import BeautifulSoup
import requests
import re

from pymongo import MongoClient

session = requests.Session()


payload = {'_username':'[YOUR_USERNAME]', 
          '_password':'[YOUR_PASSWORD]'
         }


s = session.post("https://www.chess.com/login_check", data=payload)

# Navigate to the next page and scrape the data
s = session.get('https://www.chess.com/today')

url = 'https://bn.wikipedia.org/wiki/%E0%A6%AC%E0%A6%BE%E0%A6%82%E0%A6%B2%E0%A6%BE_%E0%A6%89%E0%A6%87%E0%A6%95%E0%A6%BF%E0%A6%AA%E0%A6%BF%E0%A6%A1%E0%A6%BF%E0%A6%AF%E0%A6%BC%E0%A6%BE'
response = requests.get(url)
html = response.text
#web_text = requests.get('https://www.prothomalo.com/bangladesh/capital/%E0%A6%97%E0%A7%81%E0%A6%B2%E0%A6%BF-%E0%A6%A8%E0%A6%BF%E0%A7%9F%E0%A7%87-%E0%A6%AF%E0%A6%B6%E0%A7%8B%E0%A6%B0%E0%A6%97%E0%A6%BE%E0%A6%AE%E0%A7%80-%E0%A6%AB%E0%A7%8D%E0%A6%B2%E0%A6%BE%E0%A6%87%E0%A6%9F%E0%A7%87-%E0%A6%9A%E0%A7%9C%E0%A6%A4%E0%A7%87-%E0%A6%9A%E0%A7%87%E0%A7%9F%E0%A7%87%E0%A6%9B%E0%A6%BF%E0%A6%B2%E0%A7%87%E0%A6%A8-%E0%A6%8F%E0%A6%95-%E0%A6%A6%E0%A6%AE%E0%A7%8D%E0%A6%AA%E0%A6%A4%E0%A6%BF')
soup = BeautifulSoup(html, 'lxml')
main_text = ''
wcon = soup.find_all('div', class_='mw-body-content', limit=11)
for tc in wcon:
    main_text = tc.text
print(main_text)

cluster  = MongoClient("mongodb+srv://istiak:12345@cluster0.lqy6z.mongodb.net/test?retryWrites=true&w=majority ") 
db = cluster["test"] 
collection = db["test"] 
post = {"_id": 14, "content": main_text} 
try: 
    collection.insert_one(post) 
    print('Stored successfully') 
except: 
   print('An error occurred and quotes were not stored to db. Try changing the ID number in post') 