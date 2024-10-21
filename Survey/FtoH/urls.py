from django.urls import path
from . import views


app_name= 'FtoH'

urlpatterns = [
    path('', views.survey, name='F_H'),
    path('<str:name>/', views.increaseSelectValue, name='increaseSelection'),
]