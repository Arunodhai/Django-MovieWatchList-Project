from django import forms
from core.models import watchlist

class watchlistForm(forms.ModelForm) :
    class Meta:
        model = watchlist
        fields = '__all__'