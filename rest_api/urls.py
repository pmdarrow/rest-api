"""
rest_api URL Configuration
"""
from django.conf.urls import url
from django.views.generic import RedirectView

from users.views import Users, UserDetail

urlpatterns = [
    url(r'^$', RedirectView.as_view(pattern_name='users')),
    url(r'^users/$', Users.as_view(), name='users'),
    url(r'^users/(?P<username>\w+)/$', UserDetail.as_view(), name='user-detail')
]
