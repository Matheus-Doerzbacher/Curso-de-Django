from django.shortcuts import render


def index(request):

    outro = "Django é top2"
    context = {
        "curso": "Programação Web com Django Framework",
        "outro": outro,
    }
    return render(request, "index.html", context)


def contato(request):
    return render(request, "contato.html")
