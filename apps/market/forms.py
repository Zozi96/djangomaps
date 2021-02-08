from django.core.exceptions import ValidationError
from leaflet.forms import widgets
from django import forms
from .models import Market


class MarketForm(forms.ModelForm):

    class Meta:
        model = Market
        fields = '__all__'
        widgets = {
            'geos': widgets.LeafletWidget()
        }

    def clean_store(self):
        store = self.cleaned_data["store"]
        validate = Market.objects.filter(store=store).exists()
        if validate:
            raise ValidationError('La tienda ya está registrada')
        return store
