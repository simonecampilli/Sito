from django import forms
from .models import Post
from .models import Choice


class PostForm(forms.ModelForm):
    class Meta: #indica come deve essere il nostro modello
        model= Post
        fields = ('title', 'author', 'body')

        widgets = {  #è un dizionzario. per ogni campo specifico come deve essere
            'title': forms.TextInput(attrs={'class': 'form-control'}), # attrs={'class': 'form-control'} classe specifica di bootstrap
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            #'paragrafo': forms.Textarea(attrs={'class': 'form-control'}),

        }


class FormVoti(forms.ModelForm):
    class Meta:  # indica come deve essere il nostro modello
        model = Choice
        fields = ('question','choice_text','header_image')

        widgets = {  # è un dizionzario. per ogni campo specifico come deve essere
            'question': forms.Select(attrs={'class': 'form-control'}),
            'choice_text': forms.TextInput(attrs={'class': 'form-control'}),




        }