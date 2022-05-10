import imp
from django.urls import path
from .views import ThingsListView, ThingDetailView

urlpatterns = [
    path('things-list',ThingsListView.as_view(), name='things_list'),
    path('detail-view/<int:pk>',ThingDetailView.as_view(), name='thing_detail'),

]