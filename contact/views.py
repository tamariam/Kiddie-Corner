from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages

# Create your views here.


def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        form.save(commit=False)
        if form.is_valid():
            form.save()
            messages.success(request, 'We Received Your message, We will get back to you as soon as possible via the provided email.')
            return redirect('contact_page')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
