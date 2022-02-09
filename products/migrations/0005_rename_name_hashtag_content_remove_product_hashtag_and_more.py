# Generated by Django 4.0.2 on 2022-02-06 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_hashtag_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hashtag',
            old_name='name',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='product',
            name='hashtag',
        ),
        migrations.AddField(
            model_name='product',
            name='hashtag',
            field=models.ManyToManyField(blank=True, help_text='태그', related_name='hashtag', to='products.HashTag'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, help_text='상품 썸네일 이미지', null=True, upload_to='image'),
        ),
    ]
