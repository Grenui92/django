from django import forms
from .models import Quotes, Authors

class QuoteForm(forms.ModelForm):
    tags = forms.CharField(max_length=20,
                           required=True,
                           widget=forms.TextInput(attrs={'placeholder': 'Enter tags separated by ","'}))
    author = forms.ModelChoiceField(queryset=Authors.objects.all(),
                                    required=True)
    quote = forms.CharField(max_length=1000,
                            required=True,
                            widget=forms.TextInput())

    class Meta:
        model = Quotes
        fields = ['tags', 'author', 'quote']

    def clean_tags(self):
        tags = self.cleaned_data['tags'].split(',')
        return [tag.strip() for tag in tags]

class AuthorsForm(forms.ModelForm):
    fullname = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput())
    born_date = forms.DateField(input_formats=['%d.%m.%Y'],
                                required=True,
                                error_messages={'invalid': 'Enter date in format "dd.mm.YYYY"'})
    born_location = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput())
    description = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput())

    class Meta:
        model = Authors
        fields = ['fullname', 'born_date', 'born_location', 'description']