from django.urls import path
from . import views

urlpatterns = [
    path('', views.secret_santa_view, name='secret_santa'),
]
