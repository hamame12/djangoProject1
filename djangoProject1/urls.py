"""djangoProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import re_path

import mocktest1.views
from mocktest1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('project_list/', get_project_list),
    path('welcome/', welcome),
    re_path(r'del_project/(?P<pid>.+)', del_project),
    re_path(r'copy_project/(?P<pid>.+)', copy_project),
]
