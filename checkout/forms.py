from django import forms
from .models import Order


class CheckoutForm(forms.ModelForm):
    """
    This Form  takes payment details
    and complete an order
    """
    class Meta:
        model = Order
        fields = (
            'full_name',
            'email', 'phone_number', 'country',
            'postcode', 'town_or_city', 'street_address1',
            'street_address2', 'county',
        )
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'FULL NAME',
            'email': 'EMAIL',
            'phone_number': 'PHONE NUMBER',
            'country': 'COUNTRY',
            'postcode': 'POSTCODE',
            'town_or_city': 'TOWN OR CITY',
            'street_address1': 'STREET_ADDRESS 1',
            'street_address2': 'STREET_ADDRESS 2',
            'county': 'COUNTY',
        }
        self.fields['full_name'].widget.attrs['autofocus']=True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].widget.attrs[
                    'aria-label'] = self.fields[field].label
            else:
                self.fields[field].widget.attrs[
                    'aria-label'] = 'select a country'
            self.fields[field].widget.attrs['class'] = 'stripe-styles'
            self.fields[field].label = False

