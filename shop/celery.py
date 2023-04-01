from celery import Celery
from datetime import timedelta
from datetime import timedelta
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop.settings')

app = Celery('shop')

# app.conf.update(timezone='Europe/Kiyv')
app.config_from_object('django.conf:settings', namespace='CELERY')

# app.conf.task_routes = {'Products.tasks.*': {'queue': 'simple'}}

# app.conf.beat_schedule = {
#     'exchange_rate' : {
#         'task' : 'Products.tasks.get_currency',
#         'schedule' : timedelta(seconds=10),
#     }
# }

# task_routes = ([
#     ('Products.tasks.*', {'queue': 'simple'}),
# ],)

# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     # Calls test('hello') every 10 seconds.
#     sender.add_periodic_task(4, add.s(3, 5), name='add every 10')