Criando seu primeiro projeto
===

Você deve ter o Pytohn e o Django devidamente instalados, dê preferência para o [virtualenv](http://www.devfuria.com.br/python/virtualenv/).


No terminal do Linux, digite...

    django-admin startproject mysite


O comando acima criará a seguinte estrutura:

    mysite/                 ---> seu projeto
        manage.py           ---> um utilitário de linha de comando
        mysite/             ---> seu pacote principal
            __init__.py
            settings.py     ---> as configurações do seu projeto
            urls.py
            wsgi.py         ----> ponto de entrada (entry-point) para integrar com web server (ex: Apache)

Neste instante deveríamos esta prontos para ver um "Hello World", mas antes é preciso configurar o banco de dados.


database-setup
---

Se você analisar o arquivo `mysite/settings.py`, na seção `DATABASES` esta apontando para um arquivo em SQLite
chamado `db.sqlite3`.

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

Ele é instalado como padrão, isso ajuda pois não precisamos de maiores configurações de banco de dados, pois podermos
fazer isso mais tarde.

O que precisamos fazer é "migrar" as bases de dados da seção `INSTALLED_APPS` para o nosso bando de dados, fazemos isso
com o seguinte comando....

    $python3 manage.py migrate

Sua tela deve ser semelhanta ao exibido abaixo.

    Operations to perform:
      Apply all migrations: admin, contenttypes, auth, sessions
    Running migrations:
      Applying contenttypes.0001_initial... OK
      Applying auth.0001_initial... OK
      Applying admin.0001_initial... OK
      Applying sessions.0001_initial... OK

O que o comando fez foi olhar para `INSTALLED_APPS` e instalar as tabelas necessárias.



Hello World
---

Agora vai!

Criamos o projeto, migramos as apps, agora podemos ver tudo funcionando.

No terminal execute...

    $ python3 manage.py runserver

Seu terminal deve ser semelhanta ao exibido abaixo.

    Performing system checks...

    0 errors found
    June 02, 2015 - 15:50:53
    Django version 1.8, using settings 'mysite.settings'
    Starting development server at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
    Quit the server with CONTROL-C.

Acesse pelo navegasdor o link [http://127.0.0.1:8000/](http://127.0.0.1:8000/

Você deve ver um atarga azul com os dizeres...

    It worked!
    Congratulations on your first Django-powered page.

O Django vem com um servidor web embutido, o que fizemos foi acioná-lo. Isso significa que não precisamos de um servidor
web instalado para testarmos a aplicação. Mas não devemos usar o servidor interno no ambiente de produção, neste caso
devemos fazer o processo correto de deploy, ou seja, integrar o servidor web com o Python/Django.
