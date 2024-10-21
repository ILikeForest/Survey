from django.urls import path
from . import views


app_name= 'FtoG'

urlpatterns = [
    path('', views.survey, name='F_G'),
    path('<str:name>/', views.increaseSelectValue, name='increaseSelection'),
]