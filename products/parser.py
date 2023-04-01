from bs4 import BeautifulSoup
import requests
import lxml
import redis

RedisClient = redis.Redis(host='localhost', port=6379, db=0)

def get_currency():
    response = requests.get('https://rate.in.ua/kiev')
    soup = BeautifulSoup(response.text, 'lxml')
    content = soup.find_all('ul', class_='total-body')
    for i in content:
        domain = i.find_all('li', class_='total-icon')[0].text
        domain = (domain).replace('\n', '')
        domain = (domain).replace(' ', '')
        if domain in ('USD', 'EUR'):
            domain = i.find_all('li', class_='total-icon')[0].text
            total = i.find('span', class_='total-sell').text
            total = (total).replace('Продаж', '')
            total = (total).replace('\n', '')
            total = float(f'{total[0:2]}.{total[3:5]}')
            RedisClient.set(domain, total)
