from django.urls import path
from . import views


app_name= 'ItoD'

urlpatterns = [
    path('', views.survey, name='I_D'),
    path('<str:name>/', views.increaseSelectValue, name='increaseSelection'),
]