# SAD_Week-5
An example Django ["Hello World!"](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program) application.

[![CircleCI](https://circleci.com/gh/freemanpd/django-helloworld.svg?style=svg)](https://circleci.com/gh/freemanpd/django-helloworld)

## Screenshots

![An example Django "Hello World!" application](https://github.com/freemanpd/django-helloworld/blob/master/docs/hello-world.png)

## Requirements
1. Python 3.8+
1. Pipenv 

## Installation
1. Start Python virtual ENV
```
pipenv shell
```
2. Install dependencies
```
pipenv install
```
3. Run database migrations
```
python manage.py migrate; python manage.py makemigrations
```
4. Create admin user
```
python manage.py createsuperuser --username admin
```

## Run application
```
python manage.py runserver
```
Once the server is running, visit http://127.0.0.1:8000 in your web browser. Now, you should see something like the following:

![An example Django "Hello World!" application](https://github.com/freemanpd/django-helloworld/blob/master/docs/hello-world.png)

**Note:** access the Django admin interface here: http://127.0.0.1:8000/admin. Example:

![Django admin login](https://github.com/freemanpd/django-helloworld/blob/master/docs/django-admin-login.png)

## I use those resources down delow
* Properly installing Python - https://docs.python-guide.org/starting/installation/
* Installing pipenv - https://docs.python-guide.org/dev/virtualenvs/#installing-pipenv
* Python programming language - https://www.python.org/
* Django - https://www.djangoproject.com/
