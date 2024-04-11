from django import forms
from django.core.exceptions import ValidationError

from music.models import Musician, Genre, Tagged


class AddPageForm(forms.ModelForm):
    genre = forms.ModelChoiceField(queryset=Genre.objects.all(), empty_label='Жанр не выбран', label='Жанр')
    #tagged = forms.ModelChoiceField(queryset=Tagged.objects.all(), empty_label='Тег не выбран', label='Тег')


    class Meta:
        model = Musician
        fields = ['title', 'photo', 'slug', 'context',  'genre', 'age']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'context': forms.TextInput(attrs={'cols': 100, 'rows': 20})
        }
        labels = {'slug': 'URL'}

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise ValidationError("Длина превышает 50 символов")

        return title


class UploadFilesForm(forms.ModelForm):
    file = forms.FileField(label='Фото')
