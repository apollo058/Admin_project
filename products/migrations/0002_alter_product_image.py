# Generated by Django 4.0.2 on 2022-02-05 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(help_text='상품 썸네일 이미지', upload_to='image'),
        ),
    ]