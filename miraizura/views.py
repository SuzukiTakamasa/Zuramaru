from django.shortcuts import render

# Create your views here.
from django.views import generic
from .forms import InquiryForm
from django.urls import reverse_lazy
from django.contrib import messages
import logging

Logger = logging.getLogger(__name__)

class IndexView(generic.TemplateView):
    template_name = "index.html"

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    success_url = reverse_lazy('miraizura:inquiry')

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'The message has been sent successfully.')
        Logger.info('Inquiry send by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)








