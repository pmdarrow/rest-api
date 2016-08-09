from django.db import models

MAX_LENGTH = 255


class User(models.Model):
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
    email = models.EmailField()
    username = models.CharField(max_length=MAX_LENGTH)
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
