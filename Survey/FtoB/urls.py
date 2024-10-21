from django.urls import path
from . import views


app_name= 'FtoB'

urlpatterns = [
    path('', views.survey, name='F_B'),
    path('<str:name>/', views.increaseSelectValue, name='increaseSelection'),
]