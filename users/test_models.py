from datetime import datetime

from django.test import TestCase
from django.test.client import RequestFactory

from .models import User


class TestUserModel(TestCase):
    def test_as_dict(self):
        user = User.objects.create(
            username='foo',
            email='foo@foo.org',
            gender='male',
            title='mr',
            first_name='Foo',
            last_name='Bar',
            street='123 Main St',
            city='Nowhere',
            state='CA',
            zip=90210,
            password='foo',
            salt='foo',
            md5='foo',
            sha1='foo',
            sha256='foo',
            registered=datetime(2016, 1, 1),
            dob=datetime(1995, 1, 1),
            phone='555-5555',
            cell='444-4444',
            pps='foo',
            large_picture='http://google.com',
            medium_picture='http://google.com',
            thumbnail_picture='http://google.com',
        )
        rf = RequestFactory()
        request = rf.get('/users/')

        self.assertEqual(user.as_dict(request), {
            'detail_url': 'http://testserver/users/foo/',
            'username': 'foo',
            'email': 'foo@foo.org',
            'gender': 'male',
            'title': 'mr',
            'first_name': 'Foo',
            'last_name': 'Bar',
            'street': '123 Main St',
            'city': 'Nowhere',
            'state': 'CA',
            'zip': 90210,
            'registered': datetime(2016, 1, 1),
            'dob': datetime(1995, 1, 1),
            'phone': '555-5555',
            'cell': '444-4444',
            'pps': 'foo',
            'large_picture': 'http://google.com',
            'medium_picture': 'http://google.com',
            'thumbnail_picture': 'http://google.com',
        })
