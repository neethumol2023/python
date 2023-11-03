from django.test import TestCase
from django.urls import reverse, resolve
from ecommerce_app.views import home

class TestURL(TestCase):
    def test_urlhome(self):
        url=reverse('home')
        print("url is :",url)
        print("Resolve: ",resolve(url))
        self.assertEqual(resolve(url).func,home)
