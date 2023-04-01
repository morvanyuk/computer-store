from socket import socket
from unicodedata import name
from django.test import TestCase
from .models import *

# Create your tests here.
class CreateData(TestCase):
    def test_product(self) -> None:
        intel = Brend.objects.create(name='Intel')
        nvidia = Brend.objects.create(name='nvidia')
        # Processor.objects.create(series='Intel Core i9', socket='LGA1200', number_of_cores=10, numer_of_streams=20,
        # clock_frequency=3.5, TDP=95, video_card_model='Intel UHD Graphics 630', turbo_clock_frequency=5.2, warranty_period='1 year', brend=intel)
        # Videocard.objects.create(graphics_chip='GeForce RTX 3060', memory_frequency=15000, cooling_system='WINDFORCE 2X', memory_capacity=12,
        #  maximum_supported_resolution='7680x4320', memory_type='GDDR6', minimum_capacity=550, discharge=192, interface='282 x 117 x 41 мм', brend=nvidia)
        
        # Short
        Processor.objects.create(series='Intel Core i9', socket='LGA1200', number_of_cores=10, number_of_streams=20)
        Videocard.objects.create(graphics_chip='GeForce RTX 3060', memory_capacity=12, memory_type='GDDR6')
        