from django.urls import path
from . import views


app_name= 'BtoA'

urlpatterns = [
    path('', views.survey, name='B_A'),
    path('<str:name>/', views.increaseSelectValue, name='increaseSelection'),
]