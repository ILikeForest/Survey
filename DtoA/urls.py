from django.urls import path
from . import views


app_name= 'DtoA'

urlpatterns = [
    path('', views.survey, name='D_A'),
    path('<str:name>/', views.increaseSelectValue, name='increaseSelection'),
]