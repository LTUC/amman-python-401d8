from django.views.generic import ( ListView,
                                   CreateView,
                                   UpdateView,
                                   DeleteView,
                                   TemplateView,
                                   DetailView,
                                   View
                                    )

from .models import Thing



class HomeView(ListView):
    model = Thing
    template_name = "home.html"
    

class ThingsListView(ListView):
    template_name = "things_list.html"
    model = Thing

class ThingsDetailView(DetailView):
    template_name = "thing_detail.html"
    model = Thing


class ThingsCreateView(CreateView):
    template_name = "thing_create.html"
    model = Thing
    fields = ["name", "reviewer", "rating"]



class ThingsUpdateView(UpdateView):
    template_name = "thing_update.html"
    model = Thing
    fields = ["name", "rating"]

class ThingsDeleteView(DeleteView):
    template_name = "thing_delete.html"
    model = Thing
    success_url ='/'


# class MyCustomView(View):

#     queryset= Thing.objects.all()
#     def get(self, request, *args, **kwargs):
#         pass

#     def post(self, request, *args, **kwargs):
#         data = request.data

#         my_thing={
#             "name" : data["name"],
#             "rating" : data["rating"],

#         }

#         my_object = Thing.objects.create(**my_thing)
#         my_object.save()

#         return render(request, "home.html", {})

#     def put(self, request, *args, **kwargs):
#         pass


#     def delete(self, request, *args, **kwargs):
#         pass