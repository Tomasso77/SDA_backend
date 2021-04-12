from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


def hello(request):
    print(request)
    try:
        s = int(request.GET.get('s', ''))
    except Exception as ex:
        return HttpResponse(f"Coś poszło nie tak! Błąd: {ex}")

    tekst = f"<b>Wartość s={s}</b><br>" \
            f"<a href='/hello/?s={s+1}'>link zwiększający o 1</a><br>" \
            f"<a href='/hello/?s={s-1}'>link zmniejszający o 1</a>"
    return HttpResponse(tekst)

# 127.0.0.1:8000/hello/?s=10