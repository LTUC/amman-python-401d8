from django.urls import path
from things.api.viewset import (
                                ThingsListAPIView,
                                ThingsDetailAPIView
                                )

urlpatterns = [
    path('api/v1/things-list', ThingsListAPIView.as_view(), name='things_list'),
    path('api/v1/<int:pk>', ThingsDetailAPIView.as_view(), name='thing_detail'),

]