from rest_framework import serializers
from .models import ChwideukModel


class ChwideukSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChwideukModel
        fields = ['title']