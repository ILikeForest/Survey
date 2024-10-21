from django.urls import path
from . import views


app_name= 'DtoF'

urlpatterns = [
    path('', views.survey, name='D_F'),
    path('<str:name>/', views.increaseSelectValue, name='increaseSelection'),
]