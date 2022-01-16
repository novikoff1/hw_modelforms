from django.urls import path

from homework_here.views import Person

urlpatterns = [
    path('', Person),
]
