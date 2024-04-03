from django.shortcuts import render

from .models import Produto


def index(request):

    produtos = Produto.objects.all()
    context = {
        "produtos": produtos,
    }
    return render(request, "home/index.html", context)


def contato(request):
    return render(request, "contato/contato.html")


def produto(request, pk):
    prod = Produto.objects.get(id=pk)
    context = {
        "produto": prod,
    }
    return render(request, "produto/produto.html", context)
