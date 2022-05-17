
from multiprocessing import context
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Snack


class SnacksListView(ListView):
    template_name = 'snacks_list.html'
    model = Snack


class SnackDetailView(DetailView):
    template_name = 'snack_detail.html'
    model = Snack

# def snacks_list(request):
#     context = {}
#     snacks_list = Snack.objects.all()

#     context['snacks_list'] = snacks_list
#     return render(request, 'snacks_list.html', context)