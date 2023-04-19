from django import forms

from .models import Movie

from django.core.validators import MinValueValidator, MaxValueValidator

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('name', 'long_time', 'start_date', 'end_date', 'company',)


class GenerateRandomUserForm(forms.Form):
    total = forms.IntegerField(
        validators=[
            MinValueValidator(50),
            MaxValueValidator(5000)
        ]
    )