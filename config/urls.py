"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Main.urls')),
    path('B-A/', include('BtoA.urls')),
    path('B-G/', include('BtoG.urls')),
    path('C-F/', include('CtoF.urls')),
    path('D-A/', include('DtoA.urls')),
    path('D-F/', include('DtoF.urls')),
    path('F-A/', include('FtoA.urls')),
    path('F-B/', include('FtoB.urls')),
    path('F-G/', include('FtoG.urls')),
    path('F-H/', include('FtoH.urls')),
    path('I-C/', include('ItoC.urls')),
    path('I-D/', include('ItoD.urls')),
    path('thanks/', include('ThankYou.urls')),
]