from django.shortcuts import render
from checkbox_forms.forms import CheckboxForm
from checkbox_forms.models import CheckBox

def index(request):
    listar_check = CheckBox.objects.order_by('-id')
    
    form = CheckboxForm()
    return render(request, 'checkbox_forms/index.html', {'form': form, 'listar_check': listar_check})
    
def enviar(request):
    if request.method == 'POST':
        checkbox = CheckBox.objects.create(
            email = request.POST['email'],
            assinar = request.POST.get('assinar', 'Não desejo receber e-mail'),
        )
        return render(request, 'checkbox_forms/enviado.html', {'checkbox': checkbox})
    return render(request, 'checkbox_forms/enviado.html', {})