import json

from django.http import HttpResponse, JsonResponse
from django.views.generic import View

from .forms import UserSerializer
from .models import User


def create_or_update_user(request, user=None):
    # Parse JSON data
    try:
        data = json.loads(request.body.decode(request.encoding))
    except ValueError as e:
        return JsonResponse({'error': 'Unable to parse JSON. {}'.format(e)})

    # Validate data
    serializer = UserSerializer(data, instance=user)
    if not serializer.is_valid():
        return HttpResponse(serializer.errors.as_json(), status=400,
                            content_type='application_json')

    # Create or update user
    user = serializer.save()
    return JsonResponse(user.as_dict(request), status=200 if user else 201)


class Users(View):
    def get(self, request):
        """List users"""
        users = [user.as_dict(request) for user in User.objects.all()]
        return JsonResponse(users, safe=False, status=200)

    def post(self, request):
        """Create user"""
        return create_or_update_user(request)


class UserDetail(View):
    def dispatch(self, request, username):
        try:
            self.user = User.objects.get(username=username)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found.'}, status=404)
        return super().dispatch(request)

    def get(self, request):
        """Retrieve user"""
        return JsonResponse(self.user.as_dict(request))

    def put(self, request):
        """Update user"""
        return create_or_update_user(request, self.user)

    def delete(self, request):
        """Delete user"""
        self.user.delete()
        return JsonResponse({'status': 'User deleted.'}, status=200)
