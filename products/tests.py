from rest_framework      import status
from rest_framework.test import APITestCase

from .models import HashTag, Product


class ProductTestCase(APITestCase):
    def setUp(self):
        HashTag.objects.create(content="신상")
        HashTag.objects.create(content="특가")

    def test_product(self):
        data = {
            "name" : "test_product_01",
            "price" : 9000,
            "list_price" : 10000,
            "hashtag" : ["신상", "특가"],
            "sold_out" : False
        }
        response = self.client.post('/product', data, format='json')
        data_id = response.data['id']
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.get(f'/product/{data_id}')
        self.assertEqual(response.data['hashtag'], [HashTag.objects.get(id=h).id for h in response.data['hashtag']])

        update_data = {
            "name" : "test_pd_01",
            "hashtag" : ["특가", "할인"]
        }
        response = self.client.patch(f'/product/{data_id}', update_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['hashtag'], [HashTag.objects.get(id=h).id for h in response.data['hashtag']])

        product = Product.objects.get(id=data_id)
        self.assertEqual(update_data['hashtag'], [h.content for h in product.hashtag.all()])

        response = self.client.delete(f'/product/{data_id}')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)