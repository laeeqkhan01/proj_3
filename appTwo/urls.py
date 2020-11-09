from django.urls import path
from .views      import pageTwo, jqrydemo 

urlpatterns = [
  path('', pageTwo, name='pageTwo'),
  path('jqrydemo/', jqrydemo, name='jqrydemo'),
]
