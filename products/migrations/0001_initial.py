# Generated by Django 4.0.2 on 2022-02-05 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HashTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='상품 이름', max_length=100)),
                ('image', models.ImageField(help_text='상품 썸네일 이미지', upload_to='')),
                ('price', models.IntegerField(help_text='상품 가격')),
                ('list_price', models.IntegerField(help_text='정가')),
                ('sold_out', models.BooleanField(default=0, help_text='품절 여부')),
                ('hashtag', models.ForeignKey(help_text='태그', on_delete=django.db.models.deletion.CASCADE, to='products.hashtag')),
            ],
        ),
    ]
