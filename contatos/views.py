from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import Http404
from django.db.models import Q, Value
from django.db.models.functions import Concat
from .models import Contato

# Create your views here.


def index(request):
    # contatos = Contato.objects.all()
    contatos = Contato.objects.order_by('-id').filter(
        mostrar=True
    )
    paginator = Paginator(contatos, 5)

    paginas = request.GET.get('p')
    contatos = paginator.get_page(paginas)

    return render(request, 'contatos/index.html', {
        'contatos': contatos
    })


def ver_contato(request, contato_id):
    # contato = Contato.objects.get(id=contato_id)
    contato = get_object_or_404(Contato, id=contato_id)

    if not contato.mostrar:
        raise Http404()

    return render(request, 'contatos/visualiza_contato.html', {
        'contato': contato
    })


def busca(request):
    termo = request.GET.get('termo')

    if termo is None:
        raise Http404()

    campos = Concat('nome', Value(' '), 'sobrenome')

    """
    contatos = Contato.objects.order_by('-id').filter(
        Q(nome__icontains=termo) | Q(sobrenome__icontains=termo), # contem termo no nome OU no sobrenome
        mostrar=True
    )
    """
    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo) | Q(categoria__nome__icontains=termo)
    )
    print(contatos.query)

    paginator = Paginator(contatos, 5)

    paginas = request.GET.get('p')
    contatos = paginator.get_page(paginas)

    return render(request, 'contatos/busca.html', {
        'contatos': contatos
    })
