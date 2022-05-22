from pyexpat import model
from rest_framework import serializers
from things.models import Thing


class ThingSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','description','title')
        model = Thing


# JSON