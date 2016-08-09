from django.forms import ModelForm, fields

from .models import User


class UserSerializer(ModelForm):
    registered = fields.DateTimeField(input_formats=['%Y-%m-%dT%H:%M:%SZ'])
    dob = fields.DateTimeField(input_formats=['%Y-%m-%dT%H:%M:%SZ'])

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'gender',
            'title',
            'first_name',
            'last_name',
            'street',
            'city',
            'state',
            'zip',
            'registered',
            'dob',
            'phone',
            'cell',
            'pps',
            'large_picture',
            'medium_picture',
            'thumbnail_picture',
        ]
