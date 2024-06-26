from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages

# Create your views here.


def contact_page(request):
    """This view renders contact page """
    if not request.user.is_staff:
        if request.method == 'POST':
            form = ContactForm(data=request.POST)
            form.save(commit=False)
            if form.is_valid():
                form.save()
                messages.success(request, 'We Received Your message, We will '
                                 'get back to you as soon as possible '
                                 'via the provided email.')
                return redirect('contact_page')
        else:
            form = ContactForm()
        return render(request, 'contact/contact.html', {'form': form})
    else:
        messages.info(request, 'As a staff member you are not allowed '
                      'to  view this page')
        return redirect('home')
