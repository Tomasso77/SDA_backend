import re
from datetime import date
from django.core.exceptions import ValidationError
from django.forms import (Form,
                          CharField, ModelChoiceField, IntegerField, DateField, Textarea
                          )

from viewer.models import Genre


def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError('Value must be capitalized!')


class PastDateField(DateField):

    def validate(self, value):
        super().validate(value)
        if value > date.today():
            raise ValidationError("Future dates not allowed!")

    def clean(self, value):
        result = super().clean(value)
        return date(year=result.year, month=result.month, day=1)


class MovieForm(Form):
    title = CharField(max_length=170, validators=[capitalized_validator])
    genre = ModelChoiceField(queryset=Genre.objects)
    rating = IntegerField(min_value=1, max_value=9)
    released = PastDateField()
    description = CharField(widget=Textarea, required=False)

    def clean_description(self):
        initial = self.cleaned_data['description']
        sentences = re.sub(r'\s*\.\s*', '.', initial).split('.')
        return '. '.join(sentece.capitalize() for sentece in sentences)

    def clean(self):
        result = super().clean()
        if result['genre'].name == "Komedia" and result['rating'] > 5:
            self.add_error('genre', '')
            self.add_error('rating', '')
            raise ValidationError("Commedies are not so good to be rated over 5!")
        return result




