from django.shortcuts import render, redirect

from apps.contacts.forms import ContactForm
from apps.contacts.models import Contact


def contact_view(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/contact/')
    ctx = {
        'form': form
    }
    return render(request, 'contact.html', context=ctx)
