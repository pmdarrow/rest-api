import json

from django.test import TestCase, Client

user_1 = {
    'username': 'beautifulmouse223',
    'email': 'melissa.ferguson@example.com',
    'gender': 'female',
    'title': 'miss',
    'first_name': 'melissa',
    'last_name': 'ferguson',
    'street': '8289 novara avenue',
    'city': 'Celbridge',
    'state': 'idaho',
    'zip': 47618,
    'registered': '2002-05-25T01:18:48',
    'dob': '2002-12-03T17:59:39',
    'phone': '031-433-3489',
    'cell': '081-558-7936',
    'pps': '1140426T',
    'large_picture': 'https://randomuser.me/api/portraits/women/96.jpg',
    'medium_picture': 'https://randomuser.me/api/portraits/med/women/96.jpg',
    'thumbnail_picture': 'https://randomuser.me/api/portraits/thumb/women/96.jpg'
}

user_2 = {
    'username': 'heavybird100',
    'email': 'ben.hoffman@example.com',
    'gender': 'male',
    'title': 'mr',
    'first_name': 'ben',
    'last_name': 'hoffman',
    'street': '6066 dame street',
    'city': 'Mallow',
    'state': 'iowa',
    'zip': 74036,
    'registered': '1999-03-15T20:39:21',
    'dob': '1987-12-20T12:33:52',
    'phone': '021-074-3589',
    'cell': '081-926-8542',
    'pps': '7331821T',
    'large_picture': 'https://randomuser.me/api/portraits/men/54.jpg',
    'medium_picture': 'https://randomuser.me/api/portraits/med/men/54.jpg',
    'thumbnail_picture': 'https://randomuser.me/api/portraits/thumb/men/54.jpg'
}

user_3 = {
    'username': 'blueleopard465',
    'email': 'rose.andrews@example.com',
    'gender': 'female',
    'title': 'ms',
    'first_name': 'rose',
    'last_name': 'andrews',
    'street': '5268 dame street',
    'city': 'Kinsealy-Drinan',
    'state': 'new hampshire',
    'zip': 29779,
    'registered': '2014-01-04T06:06:37',
    'dob': '1971-07-07T03:51:38',
    'phone': '051-108-3171',
    'cell': '081-855-8055',
    'pps': '8101606T',
    'large_picture': 'https://randomuser.me/api/portraits/women/10.jpg',
    'medium_picture': 'https://randomuser.me/api/portraits/med/women/10.jpg',
    'thumbnail_picture': 'https://randomuser.me/api/portraits/thumb/women/10.jpg'
}

js = {'content_type': 'application/json'}


class TestCRUDL(TestCase):
    def setUp(self):
        self.c = Client()

    def test_create_user(self):
        # Valid user
        response = self.c.post('/users/', json.dumps(user_1), **js)
        self.assertEqual(response.status_code, 201)
        self.assertDictContainsSubset(user_1, response.json())

        # Malformed JSON
        response = self.c.post('/users/', '{usernam', **js)
        self.assertEqual(response.status_code, 400)
        self.assertTrue('error' in response.json())

        # Invalid data
        invalid_user = dict(user_2)
        del invalid_user['first_name']
        response = self.c.post('/users/', json.dumps(invalid_user), **js)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
            'first_name': [
                {'code': 'required', 'message': 'This field is required.'}
            ]
        })

        # Duplicate username and email
        response = self.c.post('/users/', json.dumps(user_1), **js)
        self.assertEqual(response.status_code, 400)
        self.assertTrue('username' in response.json())
        self.assertTrue('email' in response.json())

    def test_retrieve_user(self):
        # Valid user
        self.c.post('/users/', json.dumps(user_1), **js)
        response = self.c.get('/users/{}/'.format(user_1['username']))
        self.assertEqual(response.status_code, 200)
        self.assertDictContainsSubset(user_1, response.json())

        # User not found
        response = self.c.get('/users/foo/')
        self.assertEqual(response.status_code, 404)
        self.assertTrue('error' in response.json())

    def test_update_user(self):
        self.c.post('/users/', json.dumps(user_1), **js)

        # Valid update
        updated_user = dict(user_1)
        updated_user['first_name'] = 'Jon'

        response = self.c.put('/users/{}/'.format(updated_user['username']),
                              json.dumps(updated_user), **js)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['first_name'], 'Jon')

        # Invalid Update
        invalid_user = dict(user_1)
        del invalid_user['cell']
        response = self.c.put('/users/{}/'.format(invalid_user['username']),
                              json.dumps(invalid_user), **js)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
            'cell': [
                {'code': 'required', 'message': 'This field is required.'}
            ]
        })

    def test_delete_user(self):
        # Valid user
        self.c.post('/users/', json.dumps(user_1), **js)
        response = self.c.delete('/users/{}/'.format(user_1['username']))
        self.assertEqual(response.status_code, 200)
        self.assertTrue('status' in response.json())

        # User not found
        response = self.c.delete('/users/foo/')
        self.assertEqual(response.status_code, 404)
        self.assertTrue('error' in response.json())

    def test_list_users(self):
        self.c.post('/users/', json.dumps(user_1), **js)
        self.c.post('/users/', json.dumps(user_2), **js)
        self.c.post('/users/', json.dumps(user_3), **js)

        response = self.c.get('/users/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 3)

        self.c.delete('/users/{}/'.format(user_1['username']))
        response = self.c.get('/users/')
        self.assertEqual(len(response.json()), 2)

    def test_filter_users(self):
        self.c.post('/users/', json.dumps(user_1), **js)
        self.c.post('/users/', json.dumps(user_2), **js)
        self.c.post('/users/', json.dumps(user_3), **js)

        response = self.c.get('/users/?gender=female')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

        # Multiple filters combined
        response = self.c.get('/users/?gender=female&state=idaho')
        self.assertEqual(len(response.json()), 1)

        # Search
        response = self.c.get('/users/?street__contains=dame')
        self.assertEqual(len(response.json()), 2)
        self.assertEqual(response.json()[0]['username'], 'heavybird100')
        self.assertEqual(response.json()[1]['username'], 'blueleopard465')

        # Invalid filters ignored
        response = self.c.get('/users/?invalid_filter=3')
        self.assertEqual(len(response.json()), 3)

