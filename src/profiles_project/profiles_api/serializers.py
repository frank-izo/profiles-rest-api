from rest_framework import serializers

from . import models

class HelloSerializer(serializers.Serializer):
    """Serialises a name field for testing our APIView."""

    name = serializers.CharField(max_length=10)
