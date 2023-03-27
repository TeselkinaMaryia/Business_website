from django.test import TestCase
from . import models


class TestCantactCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        models.Cantact.objects.create(name='Sara',
                                      email='saraTerner@mail.ru',
                                      subject='Work in the company.',
                                      message='I\'d like to work in this company')

    def test_get(self):
        self.assertEqual(str(models.Cantact.objects.get(id=1)), 'saraTerner@mail.ru')
