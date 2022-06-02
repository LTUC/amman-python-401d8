from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Item


def home(request):
    user = request.user
    # meaningless_var = "Hello again"
    context={}
    context["user"] = request.user
    context["items_list"] = Item.objects.all().filter(title__icontains='First')
    return render(request, "home.html", context)


class HomeView(TemplateView):

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context["user"] = request.user
        context["items_list"] = Item.objects.all().filter(title__icontains='First')
        return render(request, "home.html", context)
