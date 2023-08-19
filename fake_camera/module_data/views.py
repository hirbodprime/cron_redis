

from rest_framework import generics
from .models import ModuleModel
from .serializers import ModuleModelSerializer

class ModuleModelList(generics.ListAPIView):
    queryset = ModuleModel.objects.all()
    serializer_class = ModuleModelSerializer
