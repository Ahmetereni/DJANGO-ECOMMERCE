# Generated by Django 5.1.7 on 2025-04-10 15:36

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_code', models.CharField(max_length=8)),
                ('blog_category', models.TextField(max_length=2048)),
                ('blog_name', models.TextField(max_length=2048)),
                ('blog_url', models.TextField(max_length=2048)),
                ('blog_owner', models.CharField(max_length=8)),
                ('blog_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('blog_media', models.FileField(blank=True, upload_to='uploaded_files')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_code', models.CharField(max_length=8)),
                ('product_name', models.TextField(max_length=2048)),
                ('product_price', models.FloatField(max_length=8)),
                ('product_price_type', models.CharField(default='m2 ya da m', max_length=8)),
                ('product_material', models.CharField(max_length=50)),
                ('product_min_en', models.CharField(default='60', max_length=8)),
                ('product_max_en', models.CharField(max_length=8)),
                ('product_min_boy', models.CharField(default='100', max_length=8)),
                ('product_max_boy', models.CharField(max_length=8)),
                ('task_media', models.FileField(blank=True, upload_to='uploaded_files')),
                ('task_background_media', models.FileField(blank=True, upload_to='uploaded_files')),
                ('task_media_3', models.FileField(blank=True, upload_to='uploaded_files')),
                ('task_media_4', models.FileField(blank=True, upload_to='uploaded_files')),
                ('product_temizlemeyontemi', models.CharField(max_length=30)),
                ('product_aciklama', models.TextField(max_length=2048)),
                ('product_urunbilgileri', models.TextField(max_length=2048)),
                ('product_ozellikler', models.TextField(max_length=2048)),
                ('product_garantibilgileri', models.TextField(max_length=2048)),
                ('product_teslimatvekargo', models.TextField(max_length=2048)),
            ],
        ),
        migrations.CreateModel(
            name='Product_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_category', models.TextField(max_length=2048)),
            ],
        ),
        migrations.CreateModel(
            name='Product_color',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_color_code', models.CharField(max_length=50)),
                ('product_color_name', models.CharField(max_length=50)),
                ('product_color_media', models.FileField(blank=True, upload_to='uploaded_files/color')),
                ('product_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='console.product')),
            ],
        ),
        migrations.CreateModel(
            name='Product_subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_subcategory', models.TextField(max_length=2048)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='console.product_category')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_subcategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='console.product_subcategory'),
        ),
    ]
