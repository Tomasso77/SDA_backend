from django.db.models import (
    CharField, Model, DateField, DateTimeField, ForeignKey, TextField, IntegerField, DO_NOTHING,
    )


class Genre(Model):
    name = CharField(max_length=128)


class Movie(Model):
    title = CharField(max_length=170)
    genre = ForeignKey(Genre, on_delete=DO_NOTHING)
    rating = IntegerField()
    released = DateField()
    description = TextField()
    created = DateTimeField(auto_now_add=True)
