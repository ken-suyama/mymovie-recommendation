from django import forms

from .models import Movies, Tag


class MoviesForm(forms.ModelForm):


    tags = forms.ModelMultipleChoiceField(label='ジャンル', widget=forms.CheckboxSelectMultiple, required=True,
        queryset=Tag.objects.all(), to_field_name='')
    class Meta:
        model = Movies
        fields = ("score", "check", "tags")