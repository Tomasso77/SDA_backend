from django.shortcuts import render
from django.http import HttpResponse
from viewer.models import Movie, Genre


def movies(request):
    gatunek = request.GET.get('gatunek', '')
    return render(
        request, template_name='movies.html',
        context={'movies': Movie.objects.filter(genre__name=gatunek).order_by('-released')}
    )


def hello(request, s0):
    s1 = request.GET.get('s1', '')
    return render(
        request, template_name='hello.html',
        context={'adjectives': [s0, s1, 'beautiful', 'wonderful'],
                 'title': s1}
        )


    # try:
    #     s = int(request.GET.get('s', ''))
    # except Exception as ex:
    #     return HttpResponse(f"Coś poszło nie tak! Błąd: {ex}")
    #
    # tekst = f"<b>Wartość s={s}</b><br>" \
    #         f"<a href='/hello/?s={s+1}'>link zwiększający o 1</a><br>" \
    #         f"<a href='/hello/?s={s-1}'>link zmniejszający o 1</a>"
    # return HttpResponse(tekst)

# 127.0.0.1:8000/hello/costam?s1=10