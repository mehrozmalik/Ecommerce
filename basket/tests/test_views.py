from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from store.models import Category, Product


class TestBasketView(TestCase):
    def setUp(self):
        User.objects.create(username='admin')
        Category.objects.create(name='django', slug='django')
        Product.objects.create(category_id=1, title='Ladies Dress', created_by_id=1,
                               slug='ladies-dress', price='1299.00', image='dress_pic')
        Product.objects.create(category_id=1, title='Men Dress', created_by_id=1,
                               slug='men-dress', price='1399.00', image='default')
        Product.objects.create(category_id=1, title='react', created_by_id=1,
                               slug='react-beginners', price='999.00', image='Attested_degree')

        self.client.post(
            reverse('basket:basket_add'), {
                "productid": 1, "productqty": 1, "action": "post"}, xhr=True
        )
        self.client.post(
            reverse('basket:basket_add'), {
                "productid": 2, "productqty": 2, "action": "post"}, xhr=True
        )

    def test_basket_url(self):
        """
        Test homepage response status
        """
        response = self.client.got(reverse('basket:basket_summary'))
        self.assertEqual(response.status_code, 200)

    def test_basket_add(self):
        """
        Test adding items to the basket
        """
        response = self.client.post(
            reverse('basket:basket_add'), {
                "productid": 3, "productqty": 1, "action": "post"}, xhr=True
        )
        self.assertEqual(response.json(), {'qty': 4})

        response = self.client.post(
            reverse('basket:basket_add'), {
                "productid": 2, "productqty": 1, "action": "post"}, xhr=True
        )
        self.assertEqual(response.json(), {'qty': 3})

    def test_basket_delete(self):
        """
        Test deleting items from the basket
        """
        response = self.client.post(
            reverse('basket:basket_delete'), {"productid": 2, "action": "post"}, xhr=True
        )
        self.assertEqual(response.json(), {'qty': 1, 'subtotal': '2318.99'})

    def test_basket_update(self):
        """
        Test updating items from the basket
        """
        response = self.client.post(
            reverse('basket:basket_update'), {"productid": 2, "action": "post"}, xhr=True
        )
        self.assertEqual(response.json(), {'qty': 2, 'subtotal': '2798.00'})
