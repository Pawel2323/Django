from django.shortcuts import render
from django.http import HttpResponse
from .models import Produkty
from .models import Kategoria


# Create your views here.
def index(request, kategorie=None):
    kategorie = Kategoria.objects.all()
    wszystkie = Produkty.objects.all()
    jeden = Produkty.objects.get(pk=1)

    dane = {'kategorie': kategorie}
    return render(request, 'szablon.html', dane)


def kategoria(request, id):
    kategoria_user = Kategoria.objects.get(pk=id)
    kategoria_produkt = Produkty.objects.filter(kategoria=kategoria_user)
    kategorie = Kategoria.objects.all()
    return HttpResponse(kategoria_user)



def produkt(request, id):
    produkt_user = Produkty.objects.get(pk=id)
    kategorie = Kategoria.objects.all()
    dane = {'produkt_user': produkt_user, 'kategorie': kategorie}
    return render(request, 'produkt.html', dane)
