from products.models import Processor, Videocard, Product, Order

from products.serializators import ProductsSerializer, VideocardSerializer, ProcessorSerializer

from django.db.models import F
from django.apps import apps
import redis

from django.contrib.contenttypes.models import ContentType

RedisClient = redis.Redis(host='localhost', port=6379, db=0)

def serialization(model, queryset, many):
    model_serializator_dict = {
        Processor : ProcessorSerializer,
        Videocard : VideocardSerializer
    }
    class_serialazer = model_serializator_dict[model]
    result = class_serialazer(queryset, many=many)
    return result

# Зміна ціни на основі курсу вибраної валюти
def modify_currency(session, queryset, many=True):
    if many == True:
        for product in queryset:
            product.price /= float(RedisClient.get(session['currency']))
    else:
        queryset.price /= float(RedisClient.get(session['currency']))
    return queryset

def get_products(request, prefix_path=None, pk=None):
    # prefix_path вказує на модель продукту
    # pk вказує на можливий продукт

    # Наприклад 
    
    if pk == None:
        model = apps.get_model('products', prefix_path[0:-1])
        queryset = model.objects.all()
        for product in queryset:
            product.price /= float(RedisClient.get(request.session['currency']))
        queryset = ProductsSerializer(queryset, model=model, many=True)
        return queryset
    else:
        model = apps.get_model('products', pk[: pk.find("-")])
        object = model.objects.get(slug=pk)
        object.price /= float(RedisClient.get(request.session['currency']))
        return object

# Filtering on /products/'something'/
def filter_of_price(queryset, min_price, max_price, currency):
    if min_price is not None and min_price != '':
        queryset = queryset.filter(price__gt=float(min_price)*currency)
    if max_price is not None and max_price != '':
        queryset = queryset.filter(price__lte=float(max_price)*currency)
    return queryset

def filter_of_parametrs(queryset, fields):
    for field in fields:
        if field is not None and field != '':
            queryset = queryset.filter()

def filters(model, fields, min_price, max_price, currency='UAH'):
    queryset = model.objects.all()
    currency_ident = float(RedisClient.get(currency))

    filter_of_parametrs(queryset, fields)

    return filter_of_price(queryset, min_price, max_price, currency_ident)


def get_model_class_from_content_type(product_model, product_id=None):
    model = apps.get_model('products', product_model.model)
    if product_id is not None:
        return model, model.object.get(pk=product_id)
    return model

# gives product based slug
def get_product_model(slug, get_model_product=False):
    object = None
    model = apps.get_model('products', slug.split("-")[0])
    try:
        object = model.objects.get(slug=slug)
    except ValueError:
        pass
    if get_model_product is True:
        return object, model
    return object

def create_order(request, order):
    for i in dict(request.data):
        if i in request.session['cart']:
            product = get_product_model(i, get_model_product=True)
            print(f'{product[1].__name__.lower()}')
            Product.objects.create(order=order, count=request.data[i], product_id=product[0].id, content_type=ContentType.objects.get(app_label='Products', model=f'{product[1].__name__.lower()}'))
    return order.id

# def report_availability(product, email):
#     print('!!1')
#     pass