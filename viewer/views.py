from django.shortcuts import render
from django.http import HttpResponse
from viewer.models import Movie, Genre
from django.views import View
from django.views.generic import TemplateView, ListView, FormView
from viewer.forms import MovieForm


class MoviesView(ListView):
    template_name = 'movies.html'
    model = Movie
    paginate_by = 20


class MovieCreateView(FormView):
    template_name = "form.html"
    form_class = MovieForm


# extra_context = {'object_list': Movie.objects.all()}

# class MoviesView(TemplateView):
#     template_name = 'movies.html'
#     extra_context = {'movies': Movie.objects.all().order_by('-released'),
#                      'title': "Wynik TemplateView"}


# class MoviesView(View):
#     def get(self, request):
#         return render(
#             request, template_name='movies.html',
#             context={'movies': Movie.objects.all().order_by('-released')}
#         )

# def movies(request):
#     return render(
#         request, template_name='movies.html',
#         context={'movies': Movie.objects.all().order_by('-released')}
#     )


def hello(request):
    s1 = request.GET.get('s1', '')
    return render(
        request, template_name='hello.html',
        context={'adjectives': [ s1, 'beautiful', 'wonderful'],
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