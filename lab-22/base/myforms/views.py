from django.core.mail import send_mail
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse

from myforms.forms import NameForm, ContactForm


def thanks(request):
    return HttpResponse("Thanks for filling out our form!")


def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            return HttpResponseRedirect(reverse('myforms:thanks'))
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})


def get_contact_data(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['info@example.com']
            if cc_myself:
                recipients.append(sender)

            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect(reverse('myforms:thanks'))
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
