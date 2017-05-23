from rest_framework import serializers
from .models import PromiseModel

class PromiseSerializer(serializers.ModelSerializer):

    class Meta:
        model = PromiseModel
        fields = ('id', 'promise', 'completed')
