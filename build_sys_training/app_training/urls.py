from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("response", views.my_response, name='my_response')
]