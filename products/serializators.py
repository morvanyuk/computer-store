from rest_framework import serializers
from products.models import Processor, Videocard, Order

class Products(serializers.Serializer):

    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)

class ProcessorSerializer(serializers.ModelSerializer):

    class Meta:
        exclude = ('id', 'count')
        model = Processor


class VideocardSerializer(serializers.ModelSerializer):

    class Meta:
        exclude = ('id', 'count', 'slug')
        model = Videocard


class ProductsSerializer(serializers.ModelSerializer):

    # price = serializer

    def __init__(self, *args, **kwargs):
        self.Meta.model = kwargs['model']
        return super().__init__(self, *args)
        
    class Meta:
        exclude = ('id', 'count',)

