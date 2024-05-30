from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """ form  for admins for  crud functionality 
    """
    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """"
        Initialise the form attributes
        """

        # taken from boutique ado walk through 
        categories = Category.objects.all()
        category_friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = category_friendly_names

        for field_name, field in self.field.items():
            field.widget.attrs['class'] = 'border-black text-light'
            self.fields['name'].widget.attrs['readonly'] = True




     

    
