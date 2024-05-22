from django.shortcuts import render
from .forms import ContactForm

# Create your views here.


def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        form.save(commit=False)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm()
        
    return render(request, 'contact/contact.html', {'form': form })