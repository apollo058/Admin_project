from django.db import models
from model_utils.models import TimeStampedModel

class HashTag(models.Model):
    content = models.CharField(max_length=50)

    def __str__(self):
        return self.content

class Product(TimeStampedModel):
    name       = models.CharField(max_length=100, help_text="상품 이름")
    image      = models.ImageField(upload_to='image', null=True, blank=True, help_text="상품 썸네일 이미지")
    price      = models.IntegerField(help_text="상품 가격")
    list_price = models.IntegerField(help_text="정가")
    hashtag    = models.ManyToManyField(HashTag, related_name='hashtag', blank=True, help_text="태그")
    sold_out   = models.BooleanField(default=0 ,help_text="품절 여부")

    def __str__(self):
        return self.name

    def discount(self):
        try:
            return round((1 - self.price / self.list_price) * 100)
        except TypeError:
            return 0

    def hashtag_content(self):
        return [h.content for h in self.hashtag.all()]