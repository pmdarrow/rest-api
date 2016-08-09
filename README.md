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
