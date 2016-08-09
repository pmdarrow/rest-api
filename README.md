# rest-api

A Django-based RESTful API for managing a directory of users.

## Bootstrapping

```
$ pip install virtualenvwrapper
$ source /usr/local/bin/virtualenvwrapper.sh
$ mkvirtualenv rest-api -p python3.4
$ pip install -r requirements.txt
```

## Starting Server

```
$ ./manage.py migrate
$ ./manage.py runserver
```

## Importing Initial User Data

```
$ ./manage.py import_users
```

## Running Tests

```
$ ./manage.py test
```

## Usage Notes

- All standard REST functionality is supported, with the exception of partial
updates via PATCH. Only complete updates with PUT are supported.
- Filtering/searching is available via query parameters:
    - Exact match: `http://localhost:8000/users/?first_name=allie`
    - Search: `http://localhost:8000/users/?street__contains=killarney`
- The user model was flattened to make the filtering API simpler. Given
some more time, filtering could be improved to support nested objects.
- Limitations: most fields can be filtered or searched with the exception of 
zip, registered, dob and URL fields. More work needs to be completed to support 
integer and date types.
- The database I selected for demo purposes is sqlite3, but this shouldn't be
used in production. I would likely use PostgreSQL or MySQL.
