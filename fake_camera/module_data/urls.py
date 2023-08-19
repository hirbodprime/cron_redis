# your_app/urls.py

from django.urls import path
from .views import ModuleModelList

urlpatterns = [
    path('camera-data/', ModuleModelList.as_view(), name='module-model-list'),
    # Other URLs for your app
]
