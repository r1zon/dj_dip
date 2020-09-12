from django import forms
from .models import Review, Product

choices = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5)
     )

class ReviewForm(forms.Form):
    name = forms.CharField(label='Имя',
                           )
    text = forms.CharField(widget=forms.Textarea(attrs={'rows':4, 'cols':40}),
                           label='Отзыв',
                           )
    rate = forms.ChoiceField(widget=forms.RadioSelect(),
                             choices=choices,
                             label='Рейтинг')


    class Meta(object):
        model = Review
        exclude = ('id', 'product')
