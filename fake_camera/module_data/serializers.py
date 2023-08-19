# your_app/serializers.py

from rest_framework import serializers
from .models import ModuleModel

class ModuleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModuleModel
        fields = '__all__'
