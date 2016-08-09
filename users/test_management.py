from io import StringIO

from django.test import TestCase

from .management.commands import import_users
from .models import User


class TestImportUsers(TestCase):
    def test_import_users(self):
        out = StringIO()
        command = import_users.Command(stdout=out)
        command.handle()
        out.seek(0)
        self.assertTrue('Successfully imported 100 users.' in out.read())
        self.assertEqual(User.objects.count(), 100)
