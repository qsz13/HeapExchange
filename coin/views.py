from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class TempView(TemplateView):
    template_name = 'coin/coin.html'