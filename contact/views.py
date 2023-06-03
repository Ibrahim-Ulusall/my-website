from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from .forms import ContactForm

class ContactView(SuccessMessageMixin,FormView):
    template_name = 'contactAppFiles/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    success_message = 'Teşekkürler! Geri Bildiriminizi aldık.'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    