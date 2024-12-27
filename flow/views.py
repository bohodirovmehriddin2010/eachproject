from django.shortcuts import render
from django.views.generic import TemplateView


class flow(TemplateView):
    template_name = 'index.html'
