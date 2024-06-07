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
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': 'Email',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Postcode',
            'town_or_city': 'Town or City',
            'street_address1': 'Street_Address 1',
            'street_address2': 'Sreet_Address 2',
            'county': 'County',
        }
        self.fields['full_name'].widget.attrs['autofocus'] = True
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
            self.fields[field].widget.attrs['class'] = 'stripe-style'
            self.fields[field].label = False
