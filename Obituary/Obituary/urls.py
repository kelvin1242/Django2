"""
URL configuration for obituary_platform project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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


# obituary_platform/urls.py

from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic import TemplateView  # Import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('submit_obituary/', include('obituaries.urls')),  # Assuming your app's URLs are in obituaries.urls
    path('view_obituaries/', include('obituaries.urls')),  # Assuming your app's URLs are in obituaries.urls
    path('', TemplateView.as_view(template_name='home.html'), name='home'),  # Define a URL pattern for the homepage
]