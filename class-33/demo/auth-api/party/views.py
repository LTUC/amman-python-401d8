from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.generics import (
                                        ListCreateAPIView
                                    )
from rest_framework.permissions import IsAuthenticated

from .models import Party
from .serializers import PartySerializer


class PartyListView(ListCreateAPIView):
    queryset = Party.objects.all()
    serializer_class = PartySerializer
    permission_classes = (IsAuthenticated,)

    # def post(self, request, *args, **kwargs):
    #     print(request.user.id)
    #     print(request.data['title'])
    #     data={
    #         "title":request['title'],
    #         "description":request['description'],
    #         "user": request.user.id

    #     }
    #     new_party = Party.objects.create(**data)
    #     new_party.save()
    #     return HttpResponse("Success")
