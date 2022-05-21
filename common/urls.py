"""djangoProject4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from .views import CurrentDateView
from .views import CurrentRandomView
from .views import CurrentHelloView
from .views import IndexView

urlpatterns = [
   path('datetime/', CurrentDateView.as_view()),
   path('random/', CurrentRandomView.as_view()),
   path('hello/', CurrentHelloView.as_view()),
   path('common', IndexView.as_view()),
]

