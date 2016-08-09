"""
rest_api URL Configuration
"""
from django.conf.urls import url
from users.views import Users

urlpatterns = [
    url(r'^$', Users.as_view(), name='users')
]
