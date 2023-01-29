from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
#  path('', RedirectView.as_view(url='/shorten/')),
  path('short/', views.get_form, name="urlform"),
  path('<short_url>', views.redirect_short_url, name="redirect_function"),
]
