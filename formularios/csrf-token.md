Cross Site Request Forgery protection (CSRF Token)
===

[https://docs.djangoproject.com/en/1.8/ref/csrf/](https://docs.djangoproject.com/en/1.8/ref/csrf/)

Ao enviar qualquer tipo de formulário pelo método POST, é obrigatório a utilização do CSRF Token afim 
de proteger o envio da requisição POST no navegador.

Para ativar o CSRF Token adicione na configuração `MIDDLEWARE_CLASSES` do arquivo `settings.py` a linha abaixo:

    ```python
    # mysite/polls/settings.py
    MIDDLEWARE_CLASSES = (
        ...
        django.middleware.csrf.CsrfViewMiddleware
    )
    ```

Existem 4 métodos para se utilizar o CSRF Token.

1. No formulário do Template HTML

    ```python
    # mysite/polls/templates/index.html
    <form action="." method="POST">
        {% csrf_token %}
        ...

    </form>
    ```


2. Em uma função especifica da View que utiliza dados enviados por POST

    ```python
    # mysite/polls/views.py
    from django.shortcuts import render_to_response
    from django.template.context_processors import csrf

    def my_view(request):
        c = {}
        c.update(csrf(request))
        # ... view code here
        return render_to_response("a_template.html", c)
    ```

3. Ao criar um arquivo de configuração `post-csrf.js` que será executado antes de enviar as requisições AJAX por POST.

    ```javascript
    // mysite/polls/templates/static/post-csrf.js
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                // Only send the token to relative URLs i.e. locally.
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    });
    ```

4. Inserindo manualmente no Template HTML e enviando o token na requisição AJAX
    
    ```python
    # mysite/polls/templates/index.html
    <div style="display:none">
        <input type="hidden" name="csrfmiddlewaretoken" value="{{ csrf_token }}">
    </div>
    ```

    ```javascript
    // mysite/polls/templates/static/script.js
    var id = that.attr("data-id");
    var csrftoken = $("input[name=csrfmiddlewaretoken]").val();
    var serialize = "csrfmiddlewaretoken="+csrftoken+"&id=" + id;

    $.post('/url/'+id+'/', serialize, function (html) {
        ...
    }
    ```

Decorators
---

###csrf_exempt

É possível desabilitar o CSRF Token em uma função especifica ao utilizar o decorator `csrf_exempt`

```python
# mysite/polls/views.py
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

@csrf_exempt
def my_view(request):
    return HttpResponse('Hello world')
```


###csrf_protect

É possível desabilitar o a verificação o CSRF do projeto para todas as requisições do tipo POST e habilitar 
somente em algumas funções que achar necessária utilizando o decorator `csrf_protect` na função.

Para desabilitar a proteção comente ou remova a linha 'django.middleware.csrf.CsrfViewMiddleware' do arquivo 
`mysite/polls/settings`.

```python
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
#   'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)
```

Lembre-se de utilizar o decorator `csrf_protect` em todas as funções que enviam e recebem as requisições por POST, 
para não ocorrer o erro 403.


```python
# mysite/polls/views.py
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render

@csrf_protect
def my_view(request):
    c = {}
    # ...
    return render(request, "a_template.html", c)
```


###requires_csrf_token

Possui a mesma função que o `csrf_protect` com a diferença de não rejeitar a requisição (não envia no erro 403).

```python
# mysite/polls/views.py
from django.views.decorators.csrf import requires_csrf_token
from django.shortcuts import render

@requires_csrf_token
def my_view(request):
    c = {}
    # ...
    return render(request, "a_template.html", c)
```