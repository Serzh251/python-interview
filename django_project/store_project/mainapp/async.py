import json

from bs4 import BeautifulSoup
import requests
import lxml

headers = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

url = (f'http://127.0.0.1:8077')

response = requests.get(url=url, headers=headers).text
soup = BeautifulSoup(response, 'lxml')
data_links = []
goods_list = []
data_goods = []
category_links = soup.find_all('a', class_='nav-link')

for item in category_links:
    try:
        link = url + item.get("href")
        data_links.append(link)
    except:
        data_links.append('no data link')

data_links.pop(0)

for item in data_links:
    try:
        response = requests.get(url=item, headers=headers).text
        soup = BeautifulSoup(response, 'lxml')
        for i in soup.find_all('div', class_='card shadow-sm'):
            goods_list.append({
                'name': i.find('h3', class_='text-center').text,
                'manufactured': i.find('h4', class_='text-center').text,
                'price': i.find('h5', class_='text-center').text,
                'category_name': i.find('h6', class_='text-center').text
            })
    except:
        goods_list.append('no data goods')


with open('goods_list.json', 'w', encoding='utf-8') as file:
    json.dump(goods_list, file, ensure_ascii=False, indent=4)
