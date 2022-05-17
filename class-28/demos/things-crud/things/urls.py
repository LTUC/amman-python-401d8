from django.urls import path
from .views import (HomeView,
                    ThingsCreateView,
                    ThingsDetailView,
                    ThingsUpdateView,
                    ThingsDeleteView
                    )

urlpatterns = [
    path('', HomeView.as_view(), name = "home"),
    path('create/', ThingsCreateView.as_view(), name = "create_thing"),
    path('<int:pk>', ThingsDetailView.as_view(), name = "detail_thing"),
    path('hi/<int:pk>', ThingsUpdateView.as_view(), name = "update_thing"),
    path('delete/<int:pk>', ThingsDeleteView.as_view(), name = "delete_thing"),
]