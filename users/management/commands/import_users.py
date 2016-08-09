from datetime import datetime
import json
import os

from django.core.management.base import BaseCommand
from django.conf import settings

from users.models import User


class Command(BaseCommand):
    help = 'Imports a set of users from users.json'

    def handle(self, *args, **options):
        users_file = os.path.join(settings.BASE_DIR, 'users.json')
        user_total = 0
        with open(users_file) as f:
            data = json.load(f)
            for result in data['results']:
                user_total += 1
                user = result['user']
                User.objects.create(
                    gender=user['gender'],
                    title=user['name']['title'],
                    first_name=user['name']['first'],
                    last_name=user['name']['last'],
                    street=user['location']['street'],
                    city=user['location']['city'],
                    state=user['location']['state'],
                    zip=user['location']['zip'],
                    email=user['email'],
                    username=user['username'],
                    password=user['password'],
                    salt=user['salt'],
                    md5=user['md5'],
                    sha1=user['sha1'],
                    sha256=user['sha256'],
                    registered=datetime.fromtimestamp(user['registered']),
                    dob=datetime.fromtimestamp(user['dob']),
                    phone=user['phone'],
                    cell=user['cell'],
                    pps=user['PPS'],
                    large_picture=user['picture']['large'],
                    medium_picture=user['picture']['medium'],
                    thumbnail_picture=user['picture']['thumbnail'],
                )

        self.stdout.write(self.style.SUCCESS(
            'Successfully imported %s users.' % user_total))
