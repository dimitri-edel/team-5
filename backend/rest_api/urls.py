"""rest_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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


    IMPORTANT: urls.py should not handle static files.
"""

from django.contrib import admin
from django.urls import path, include
from rest_api import views
from django.conf.urls import handler404, handler500
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='test/', permanent=False), name='index'),
    path('test/', views.APITest.as_view(), name='api-test'),
    path('admin/', admin.site.urls),
    path('profile/', include('rest_api.user_profile.urls')),
    path('likes/', include('rest_api.likes.urls')),
]

handler404 = 'rest_api.views.custom_error_404'
handler500 = 'rest_api.views.custom_error_500'
