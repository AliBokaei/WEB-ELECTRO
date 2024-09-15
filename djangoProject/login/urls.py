from django.template.context_processors import static
from django.urls import path

from djangoProject import settings
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.loginView)
]
