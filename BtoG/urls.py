from django.urls import path
from . import views


app_name= 'BtoG'

urlpatterns = [
    path('', views.survey, name='B_G'),
    path('<str:name>/', views.increaseSelectValue, name='increaseSelection'),
]
