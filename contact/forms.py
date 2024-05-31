from django import forms
from .models import UserMessage


class ContactForm(forms.ModelForm):
    """
    This Form handles contact form submission
    """
    class Meta:
        model = UserMessage
        fields = (
         'name', 'email',
         'message', 'subject',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': 'Name',
            'email': 'Email',
            'subject': 'Subject',
            'message': 'Message',
        }

        self.fields['name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs[
                'aria-label'] = self.fields[field].label
            self.fields[field].label = False
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'text light bg-white'
