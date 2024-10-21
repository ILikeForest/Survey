from django.urls import path
from . import views


app_name= 'FtoA'

urlpatterns = [
    path('', views.survey, name='F_A'),
    path('<str:name>/', views.increaseSelectValue, name='increaseSelection'),
]