from products.models import Processor, Videocard, Brend

Brend.objects.update_or_create(name='Intel')
Brend.objects.update_or_create(name='Nvidia')

# Processor.objects.update_or_create(series='Intel Core i9', socket='LGA1200', number_of_cores=10, numer_of_streams=20,
# clock_frequency=3.5, TDP=95, video_card_model='Intel UHD Graphics 630', turbo_clock_frequency=5.2, warranty_period='1 year', brend__name='Intel')
# Videocard.objects.update_or_create(graphics_chip='GeForce RTX 3060', memory_frequency=15000, cooling_system='WINDFORCE 2X', memory_capacity=12,
#  maximum_supported_resolution='7680x4320', memory_type='GDDR6', minimum_capacity=550, discharge=192, interface='282 x 117 x 41 мм', brend__name='Videocard')

# Short
Processor.objects.update_or_create(series='Intel Core i9-10900KF', socket='Socket 1200', number_of_cores=10, number_of_streams=20, brend__name='Intel', price=15182)
Processor.objects.update_or_create(series='Intel Core i5-10400F', socket='Socket 1200', number_of_cores=6, number_of_streams=12, brend__name='Intel', price=5883)
Processor.objects.update_or_create(series='Intel Core i7-10700F', socket='Socket 1200', number_of_cores=8, number_of_streams=16, brend__name='Intel', price=12820)
Processor.objects.update_or_create(series='Core i3-10100', socket='Socket 1200', number_of_cores=4, number_of_streams=8, brend__name='Intel', price=4669)
Processor.objects.update_or_create(series='Intel Celeron G5905', socket='Socket 1200', number_of_cores=2, number_of_streams=2, brend__name='Intel', price=1560)
Processor.objects.update_or_create(series='Intel Pentium Gold G7400', socket='Socket 1700', number_of_cores=2, number_of_streams=4, brend__name='Intel', price=3642)

Videocard.objects.update_or_create(graphics_chip='GeForce RTX 3060', memory_capacity=12, memory_type='GDDR6', brend__name='Videocard', price=20350)
Videocard.objects.update_or_create(graphics_chip='GeForce GTX 1660 Super D6 6G', memory_capacity=6, memory_type='GDDR6', brend__name='Videocard', price=12099)
Videocard.objects.update_or_create(graphics_chip='GeForce GTX 1650 GamingPro', memory_capacity=4, memory_type='GDDR6', brend__name='Videocard', price=8809)
Videocard.objects.update_or_create(graphics_chip='Quadro RTX4000', memory_capacity=8, memory_type='GDDR6', brend__name='Videocard', price=38029)
Videocard.objects.update_or_create(graphics_chip='GeForce RTX 2060 SUPER', memory_capacity=8, memory_type='GDDR6', brend__name='Videocard', price=18990)      