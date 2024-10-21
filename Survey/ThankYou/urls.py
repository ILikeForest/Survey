from django.urls import path
from . import views


app_name='ThankYou'

urlpatterns = [
    path('', views.thank, name='thanks')
]
