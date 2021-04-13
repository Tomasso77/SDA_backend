
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




