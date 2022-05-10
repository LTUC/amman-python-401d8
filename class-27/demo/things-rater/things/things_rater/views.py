from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Thing


class ThingsListView(ListView):
    template_name = "things_list.html"
    model = Thing
    context_object_name = "things_list"


class ThingDetailView(DetailView):
    template_name = "thing_detail.html"
    model = Thing