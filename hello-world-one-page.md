Hello World de uma única página
===

Exemplo estraído do livro Django Essencial de Julia Elman e Mark Lavin.

Trata-se de um "Hello World" de um único script.

    cd project_name
    python project_name.py runserver

[http://localhost:8000/](http://localhost:8000/)

Veja o repositório dos códigos do livro no git:

- https://github.com/lightweightdjango/examples


```python
""" project_name/project_name.py"""
import os
import sys

from django.conf import settings

DEBUG = os.environ.get('DEBUG', 'on') == 'on'

SECRET_KEY = os.environ.get('SECRET_KEY', '{{ secret_key }}')

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)

from django.conf.urls import url
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse


def index(request):
    return HttpResponse('Hello World')


urlpatterns = (
    url(r'^$', index),
)


application = get_wsgi_application()


if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
```