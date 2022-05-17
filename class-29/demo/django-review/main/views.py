from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
# project imports
from .models import Item, Meal
# from .utils import email_sender
# # third party import
# import pandas

# # built in packages imports
# import json


def home_view(request):
    name = request.GET.get("name")
    age = request.GET.get("age")
    salary = int(request.GET.get("salary"))
    salary_after_tax = salary *.8
    return HttpResponse(f"Hello I'm {name}, I'm {age} years old, my salary after tax is {salary_after_tax}")


def items_list_view(request):
    items_list = Item.objects.all()
    meals_list = Meal.objects.all()
    context = {}
    context['bla_bla_list'] = items_list
    context['meals_list'] = meals_list

    return render(request, "items_list.html", context)


class ItemsView(View):

    def get(self, request, *args, **kwargs):
        print(request.user)
        print(request.GET.get("fav_color"))
        user =request.user
        return HttpResponse(f"Hey I'm {user}")