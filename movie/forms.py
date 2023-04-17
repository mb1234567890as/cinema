from django import forms

from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ('name', 'long_time', 'start_date', 'end_date', 'company',)