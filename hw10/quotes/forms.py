from django.forms import ModelForm, CharField, TextInput, DateTimeField, ModelChoiceField
from .models import Tag, Author, Quote


class TagForm(ModelForm):
    name = CharField(min_length=3, max_length=50, required=True, widget=TextInput())

    class Meta:
        model = Tag
        fields = ['name']


class AuthorForm(ModelForm):
    fullname = CharField(min_length=3, max_length=50, required=True, widget=TextInput())
    born_date = DateTimeField()
    born_location = CharField(max_length=150, widget=TextInput)
    description = CharField(widget=TextInput)

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']


class QuoteForm(ModelForm):
    quote = CharField(min_length=5, max_length=50, required=True, widget=TextInput())
    author = ModelChoiceField(queryset=Author.objects.all(), empty_label="Select an author")


    class Meta:
        model = Quote
        fields = ['quote', 'author']
        exclude = ['tags']
