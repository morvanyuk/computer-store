import celery
from celery.utils.log import get_task_logger
import requests
import redis
from datetime import timedelta
from bs4 import BeautifulSoup
from shop.celery import app
import time

RedisClient = redis.Redis(host='localhost', port=6379, db=0)

logger = get_task_logger(__name__)

@app.task(bind=True, default_retry_delay=3, max_retries=3, autoretry_for=(ZeroDivisionError,))
def report_availability(self, email, fdfd):
    # 3 / 0
    logger.info('Adding {0} + {1}'.format(email, fdfd))
    return 0

# @app.add_periodic_task(schedule=timedelta(seconds=30))
@app.task
def get_currency():
    # response = requests.get('https://rate.in.ua/kiev')
    # soup = BeautifulSoup(response.text, 'lxml')
    # content = soup.find_all('ul', class_='total-body')
    # for i in content:
    #     domain = i.find_all('li', class_='total-icon')[0].text
    #     domain = (domain).replace('\n', '')
    #     domain = (domain).replace(' ', '')
    #     if domain in ('USD', 'EUR'):
    #         domain = i.find_all('li', class_='total-icon')[0].text
    #         total = i.find('span', class_='total-sell').text
    #         total = (total).replace('Продаж', '')
    #         total = (total).replace('\n', '')
    #         total = float(f'{total[0:2]}.{total[3:5]}')  
    #         RedisClient.set(domain, total)
    print(200)         
    RedisClient.set('USD', 200)  
