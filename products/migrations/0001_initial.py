# Generated by Django 4.1.4 on 2023-02-18 17:19

from django.db import migrations, models
import django.db.models.deletion
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225, null=True)),
                ('image', models.ImageField(null=True, upload_to='', validators=[products.models.validate_image])),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(blank=True, max_length=225, null=True)),
                ('adress', models.CharField(blank=True, max_length=225, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225, null=True)),
                ('images', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Videocard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='Images/', validators=[products.models.validate_image])),
                ('count', models.IntegerField(default=0)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('graphics_chip', models.CharField(blank=True, help_text='Введіть назву відеокарти', max_length=225, null=True)),
                ('memory_capacity', models.IntegerField(blank=True, help_text="Введіть обсяг пам'яті відеокарти", null=True)),
                ('memory_type', models.CharField(blank=True, help_text="Введіть тип пам'яті відеокарти", max_length=225, null=True)),
                ('brend', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='products.brend')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(blank=True, null=True)),
                ('product_id', models.IntegerField(null=True)),
                ('content_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.order')),
            ],
        ),
        migrations.CreateModel(
            name='Processor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='Images/', validators=[products.models.validate_image])),
                ('count', models.IntegerField(default=0)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('series', models.CharField(blank=True, max_length=225, null=True, unique=True)),
                ('socket', models.CharField(blank=True, max_length=225, null=True)),
                ('number_of_cores', models.IntegerField(blank=True, help_text='Кількість ядер', null=True)),
                ('number_of_streams', models.IntegerField(blank=True, help_text='Кількість потоків', null=True)),
                ('brend', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='products.brend')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='order',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='products.region'),
        ),
    ]
