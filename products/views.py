from django.shortcuts import render, redirect
from django.db.models import F, Q
from django.shortcuts import get_object_or_404
from django.http import Http404
from django.urls import reverse_lazy
from django.apps import apps

from django.core.mail import send_mail
from django.conf import settings

from products.tasks import report_availability
# from Products.forms import OrderDataForm
from products.servises import *
from products.serializators import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.generic.edit import FormMixin, ModelFormMixin
from django.views.generic.base import ContextMixin
# from .full import *
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, TemplateView, View, FormView
from django.urls import resolve
import time
from products.models import *
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import RetrieveAPIView
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

class ProductsList(APIView):

    def get(self, request, *args, **kwargs):
        try:
            model = apps.get_model('products', kwargs.get('model')[0:-1])
        except LookupError:
            return Response("Такої катигорії не існує")
        # Change currency
        queryset = modify_currency(session=request.session, queryset=model.objects.all())
        # Serialization queryset
        queryset = serialization(model=model, queryset=queryset, many=True)

        return Response(queryset.data, 200)

class AloneProduct(APIView):

    def get(self, request, *args, **kwargs):
        try:
            model = apps.get_model('products', kwargs.get('model')[0:-1])
            object = model.objects.get(slug=kwargs.get('key'))
        except LookupError:
            return Response("Такої катигорії або продукту не існує")
        # Change currency
        object = modify_currency(session=request.session, queryset=object, many=False)
        # Serialization queryset
        object = serialization(model=model, queryset=object, many=False)
        return Response(object.data, 200)

class show_product(RetrieveAPIView):
    # queryset = Videocard.objects.last()
    lookup_field = 'key'
    serializer_class = VideocardSerializer

    # def get(self, request, *args, *kwargs):
    #     # object = get_product_model(kwargs.get('key'))
    #     object = Videocard.objects.last()
    #     product = VideocardSerializer(object)
    #     return Response(product.data)*

class Cart(APIView):

    def get(self, request, *args, **kwargs):
        queryset = []
        if 'cart' in self.request.session:
            for product in self.request.session['cart']:
                # Get product object and her model
                product_object, model = get_product_model(product, get_model_product=True)

                product_object = modify_currency(queryset=product_object, session=request.session, many=False)
                product_object = serialization(model=model, queryset=product_object, many=False)

                queryset.append(product_object.data)
        return Response(queryset)

class Orders(TemplateView):
    template_name = 'Products/orders.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['orders'] = []
        for i in self.request.session['orders']:
            print(Order.objects.get(pk=i))
            context['orders'].append(Order.objects.get(pk=i))
    
        return context
# Rest

class Change_Currency(APIView):
    def get(self, request, *args, **kwargs):
        currency = kwargs['currency']
        request.session['currency'] = currency
        return Response(request.session)

class Add_Or_Del_From_Cart(APIView):

    def get(self, request, *args, **kwargs):
        if resolve(request.path_info).url_name == 'add_to_cart':
            product = get_product_model(kwargs.get('key'))
            if 'cart' not in request.session:   
                request.session['cart'] = []
            if product.slug not in request.session['cart'] and product.count > 0:
                request.session['cart'].append(product.slug)
            elif product.count <= 0:
                # send_mail('A cool subject', 'A stunning message', settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
                # report_availability('dsdss', 'fdsd').apply_async()
                pass
        elif resolve(request.path_info).url_name == 'del_from_cart':
            product = get_product_model(kwargs.get('key'))
            request.session['cart'].remove(product.slug)
        request.session.save()
        return Response(request.session, 200)

class Add_Or_Del_Order(APIView):

    def put(self, request, format=None):
        if 'cart' in request.session:
            # order = OrderDataForm(data=request.data)
            # if order.is_valid(raise_exception=True):
            #     order_object = order.save()
            #     request.session['orders'] = []
            #     request.session['orders'].append(create_order(request, order_object))
            return Response(200)
        return Response(403)