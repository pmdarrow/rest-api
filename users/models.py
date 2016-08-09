from collections import OrderedDict

from django.core.urlresolvers import reverse
from django.db import models

MAX_LENGTH = 255


class User(models.Model):
    username = models.CharField(max_length=MAX_LENGTH, unique=True)
    email = models.EmailField(unique=True)
    gender = models.CharField(
        choices=[('male', 'Male'), ('female', 'Female')],
        max_length=6
    )
    title = models.CharField(max_length=10)
    first_name = models.CharField(max_length=MAX_LENGTH)
    last_name = models.CharField(max_length=MAX_LENGTH)
    street = models.CharField(max_length=MAX_LENGTH)
    city = models.CharField(max_length=MAX_LENGTH)
    state = models.CharField(max_length=MAX_LENGTH)
    zip = models.IntegerField()

    # The following fields are not exposed via the API for security
    password = models.CharField(max_length=MAX_LENGTH)
    salt = models.CharField(max_length=MAX_LENGTH)
    md5 = models.CharField(max_length=MAX_LENGTH)
    sha1 = models.CharField(max_length=MAX_LENGTH)
    sha256 = models.CharField(max_length=MAX_LENGTH)

    registered = models.DateTimeField()
    dob = models.DateTimeField()
    phone = models.CharField(max_length=MAX_LENGTH)
    cell = models.CharField(max_length=MAX_LENGTH)
    pps = models.CharField(max_length=MAX_LENGTH)
    large_picture = models.URLField()
    medium_picture = models.URLField()
    thumbnail_picture = models.URLField()

    def as_dict(self, request):
        # Get relative URL for user detail
        relative_url = reverse('user-detail',
                               kwargs={'username': self.username})

        # Build absolute URL
        absolute_url = request.build_absolute_uri(relative_url)

        return OrderedDict([
            ('username', self.username),
            ('email', self.email),
            ('detail_url', absolute_url),
            ('gender', self.gender),
            ('title', self.title),
            ('first_name', self.first_name),
            ('last_name', self.last_name),
            ('street', self.street),
            ('city', self.city),
            ('state', self.state),
            ('zip', self.zip),
            ('registered', self.registered),
            ('dob', self.dob),
            ('phone', self.phone),
            ('cell', self.cell),
            ('pps', self.pps),
            ('large_picture', self.large_picture),
            ('medium_picture', self.medium_picture),
            ('thumbnail_picture', self.thumbnail_picture),
        ])
