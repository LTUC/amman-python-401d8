from rest_framework import generics
from .serializers import ThingSerializer
from things.models import Thing


class ThingsListAPIView(generics.ListCreateAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer


class ThingsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer

