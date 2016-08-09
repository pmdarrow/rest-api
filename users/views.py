from django.http import HttpResponse
from django.views.generic import View


class Users(View):
    def get(self, request):
        # <view logic>
        return HttpResponse('result')
