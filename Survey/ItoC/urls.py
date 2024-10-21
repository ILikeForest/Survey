from django.urls import path
from . import views


app_name= 'ItoC'

urlpatterns = [
    path('', views.survey, name='I_C'),
    path('<str:name>/', views.increaseSelectValue, name='increaseSelection'),
]