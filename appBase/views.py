from django.shortcuts import render, get_object_or_404

from .models import Produto
from django.template import loader
from django.http import HttpResponse


def index(request):
    produtos = Produto.objects.all()
    context = {
        "produtos": produtos,
    }
    return render(request, "home/index.html", context)


def contato(request):
    return render(request, "contato/contato.html")


def produto(request, pk):
    # prod = Produto.objects.get(id=pk)
    prod = get_object_or_404(Produto, id=pk)
    context = {
        "produto": prod,
    }
    return render(request, "produto/produto.html", context)


def error404(request, exception):
    template = loader.get_template("error/error404.html")
    return HttpResponse(
        content=template.render(request),
        content_type="text/html; charset=utf8",
        status=404,
    )


def error500(request):
    template = loader.get_template("error/error500.html")
    return HttpResponse(
        content=template.render(),
        content_type="text/html; charset=utf8",
        status=500,
    )
