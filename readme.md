RESTful API

/movie/ -> GET -> Read(List)
        -> POST [JSON] -> Create
/movie/{id}/ -> GET -> Read(Retrieve)
           -> PUT/PATCH [JSON] -> Update / Partial Update
           -> DELETE -> Delete



JSON:

{
"title": "Shrek 2",
"genre": 3,
"rating": 5,
"description": "To jest jakiś opis filmu",
"released": "2020-01-05",
"image":"http:/127.0.0.1:8000/movie/movie_40/gladiator.jpg"
}




###########################3
request.POST <- 

request.FILES


model (ORM) -> tabele w DB

1. (Create) Utworzyć rekordy 
   Movie.objects.create(title="costam", ....)
   film = Movie.objects(title=....) -> film.save()
2. (Retrieve) Pobrać (jeden, wiele) rekordów na podstawie np. filtrowania itp.
Model.objects.get(...) -> zwraca nam jeden obiekt!
   Model.objects.filter(....) -> zwaraca QuerySet (specyficzną listę obiektów/rekordów)

3. (Update) Modyfikacja rekordu 
4. (Delete) Usuwanie rekordu

CRUD

Władca Pierścieni, 2001, Fantasy
Lot nad kukułczym gniazdem, 1975, Dramat
Django, 2012, Dramat
Pulp Fiction, 1994, Dramat
Skazani na Shawshank, 1994, Dramat
Fight Club, 1999, Dramat

python manage.py shell




