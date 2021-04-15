from django.forms import (Form,
                          CharField, ModelChoiceField, IntegerField, DateField, Textarea
                          )

from viewer.models import Genre


class MovieForm(Form):
    title = CharField(max_length=170)
    genre = ModelChoiceField(queryset=Genre.objects)
    rating = IntegerField(min_value=1, max_value=9)
    released = DateField()
    description = CharField(widget=Textarea, required=False)