from django.urls import path
from .views import flow


urlpatterns = [
     path('', flow.as_view())
]
