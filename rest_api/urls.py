from django.urls import path
from rest_api.views import test
urlpatterns = [
    path("api",test)
]
