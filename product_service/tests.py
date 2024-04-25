from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Product, SERVICE


class ProductAPITest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.prdouct1 = Product.objects.create(
            NAME='PRODUCT 1',
            SLUG='PRODUCT-1',
            SHORT_DESCRIPTION='short description for product 1'
        )

        self.product2 = Product.objects.create(
            NAME='PRODUCT 2',
            SLUG='PRODUCT-2',
            SHORT_DESCRIPTION='short decritption for product 2'
        )

    def test_get_product_list(self):
        url = reverse('productsss')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    # future development
    # def test_get_product_list_detail(self):
    #     url = reverse('api/v1/products-services/products')


class ServiceAPITest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.service1 = SERVICE.objects.create(
            NAME='SERVICE 1',
            SLUG='SERVICE-1-IT-IS',
            SHORT_DESCRIPTION='SHORT DESCRIPTION IT IS'
        )
        self.service2 = SERVICE.objects.create(
            NAME='Service 2',
            SLUG='service-2',
            SHORT_DESCRIPTION='Short description for service 2'
        )

    def test_get_service_list(self):
        url = reverse('servicess')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data[0]['NAME'], 'SERVICE 1')
