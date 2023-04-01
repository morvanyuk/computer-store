from django.db import models
from django.core.files.images import get_image_dimensions
from django.core import validators
from PIL import Image
from django.db.models import F
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils.text import slugify

def validate_image(image):
    min_height = 256
    min_width = 240
    width, height = get_image_dimensions(image)
    if width < min_width or height < min_height:
        raise validators.ValidationError("Height or Width is larger than what is allowed")
    if not height / width * 100 in range(90, 105):
        print(height / width * 100)
        raise validators.ValidationError("Bad extension, the width should be 90 -105% of the height")

class BaseModel(models.Model):
    image = models.ImageField(upload_to='Images/', null=True, validators=[validate_image])
    count = models.IntegerField(default=0)
    price = models.IntegerField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, unique=True)

    class Meta:
        abstract = True

class Processor(BaseModel):

    FIELDS_FOR_FILTERING = {'number_of_cores', 'number_of_streams'}

    series = models.CharField(max_length=225, null=True, blank=True, unique=True)
    socket = models.CharField(max_length=225, null=True, blank=True)
    number_of_cores = models.IntegerField(null=True, blank=True, help_text='Кількість ядер')
    number_of_streams = models.IntegerField(null=True, blank=True, help_text='Кількість потоків')
    # clock_frequency = models.FloatField(null=True, blank=True, verbose_name='Clock frequency in GHz')
    # TDP = models.IntegerField(null=True, blank=True)
    # video_card_model = models.CharField(max_length=225, null=True, blank=True)
    # turbo_clock_frequency = models.FloatField(null=True, blank=True)
    # warranty_period = models.CharField(max_length=20, null=True, blank=True)

    brend = models.ForeignKey('Brend', null=True, blank=True, on_delete=models.PROTECT)
    

    def __str__(self) -> str:
        return self.series

    def save(self, **kwargs) -> None:
        name = slugify(self.series)
        self.slug = f'processor-{name}'
        return super().save()

class Videocard(BaseModel):

    FIELDS_FOR_FILTERING = {'memory_capacity'}

    graphics_chip = models.CharField(max_length=225, null=True, blank=True, help_text='Введіть назву відеокарти')
    # memory_frequency = models.IntegerField(null=True, blank=True, help_text='')
    # cooling_system = models.CharField(max_length=225, null=True, blank=True)
    memory_capacity = models.IntegerField(null=True, blank=True, help_text="Введіть обсяг пам'яті відеокарти")
    # maximum_supported_resolution = models.CharField(max_length=225, null=True, blank=True)
    memory_type = models.CharField(max_length=225, null=True, blank=True, help_text="Введіть тип пам'яті відеокарти")
    # minimum_capacity = models.IntegerField(null=True, blank=True, verbose_name='The minimum required capacity of the BZ')
    # discharge = models.IntegerField(null=True, blank=True, verbose_name='Bit rate of the memory bus')
    # interface = models.CharField(max_length=225, null=True, blank=True)
    # dimensions = models.CharField(max_length=225, null=True, blank=True)

    brend = models.ForeignKey('Brend', null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self) -> str:
        return self.graphics_chip

    def save(self, **kwargs) -> None:
        name = slugify(self.graphics_chip)
        self.slug = f'videocard-{name}'
        return super().save()

class Brend(models.Model):
    name = models.CharField(max_length=225, null=True)
    image = models.ImageField(null=True, validators=[validate_image])

    def __str__(self) -> str:
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=225, null=True)
    images = models.ImageField(null=True)

class Order(models.Model):
    region = models.ForeignKey('Region', on_delete=models.PROTECT, null=True)
    city = models.CharField(max_length=225, null=True, blank=True)
    adress = models.CharField(max_length=225, null=True, blank=True)

class Product(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE, null=True, blank=True)
    count = models.IntegerField(null=True, blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True)
    product_id = models.IntegerField(null=True)
