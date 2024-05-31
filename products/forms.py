from django import forms
from .models import Product, Category


class ProductForm(forms.ModelForm):
    """ form  for admins for  crud functionality 
    """
    class Meta:
        model = Product
        fields = (
            'category', 'name', 'sku', 'price',
            'rating', 'in_stock', 'has_sale', 'description',
            'image',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """"
        Initialise the form attributes
        """

        # taken from boutique ado walk through  to get friendly names
        categories = Category.objects.all()
        category_friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = category_friendly_names

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black text-dark bg-white'
            self.fields['name'].widget.attrs['readonly'] = False




     

    
