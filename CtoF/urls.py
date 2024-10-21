from django.urls import path
from . import views


app_name= 'CtoF'

urlpatterns = [
    path('', views.survey, name='C_F'),
    path('<str:name>/', views.increaseSelectValue, name='increaseSelection'),
]