from django.urls import path
from .views import home_view, items_list_view, ItemsView

urlpatterns = [
    path('', home_view, name = "home"),
    path('abc', items_list_view, name = "items_list"),
    path('custom-items-view', ItemsView.as_view(), name = "xyz"),


]

# Class based views: HomeView ---> HomeView.as_view()
# Function based views: home_view