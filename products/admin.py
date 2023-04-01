from django.contrib import admin
from products.models import *

class ProcesorAdmin(admin.ModelAdmin):
    list_display = ['series', 'count']
    list_display_links = ['series',]

class VideocardAdmin(admin.ModelAdmin):
    list_display = ['graphics_chip', 'count']
    list_display_links = ['graphics_chip',]


# admin.site.register(Brend)
admin.site.register(Processor, ProcesorAdmin)
admin.site.register(Videocard, VideocardAdmin)
# admin.site.register(Order)
# admin.site.register(Product)
# admin.site.register(Region)
# Register your models here.
