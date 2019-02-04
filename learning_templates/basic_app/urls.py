from django.urls import path
from . import views

#this is for template tagging, look at html realtive_url_templates.html
app_name = 'basic_app'

urlpatterns = [
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
]
