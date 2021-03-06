"""MobileZoo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from searchImage import views as searchImage_views
from animalInfo import views as animalInfo_views
from searchModel import views as searchModel_views

urlpatterns = [
    path("upload/", searchImage_views.upload),
    path("getStatus/", searchImage_views.getStatus),
    path("animalInfo/<str:id>/", animalInfo_views.index),
    path("getPic/<str:id>/", searchImage_views.getPic),
    path("admin/", admin.site.urls),
    path("reconstruct/", searchModel_views.requestModel),
]
