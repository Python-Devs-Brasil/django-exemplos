13. Django Forms: Combobox Multi

Neste exemplo é mostrado como utilizar a classe Forms do Django para criar formulários baseado no model da aplicação.

Exemplo de uma lista por combobox, onde possível selecionar vários itens e salvar como um array list no banco de dados.

No arquivo `settings.py` é adicionado o model do projeto no `INSTALLED_APPS` para criar as tabelas do arquivo `models.py`.

Para criar a tabela do Model digite no terminal os seguintes comandos:

    python manage.py makemigrations nome-da-model
    python manage.py migrate

Arquivos alterados ou adicionados:

    /f13_combobox_multi_forms
        urls.py
        settings.py
        views.py
        models.py
        forms.py
    /templates/
        f13_combobox_multi_forms/
            index.html
            enviado.html