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
    path('project_list/', get_project_list),  # 项目列表界面
    path('welcome/', welcome),
    re_path(r'del_project/(?P<pid>.+)', del_project),  # 删除项目
    re_path(r'copy_project/(?P<pid>.+)', copy_project),  # 复制项目
    path('login/', login),  # 访问登陆页面
    path('', login, name="home"),  # 默认登录页面
    re_path(r'^accounts/login/$', login),  # 没有登录时，访问其他网址默认跳转到登录页面
    path('sign_in_action/', login_action),  # 登录时请求
    path('send_mail_code/', send_mail_code_action),  # 发送验证码邮件
    path('sign_up_action/', register_action),  # 注册时请求
    re_path(r'.+/logout/', logout),  # 登陆注销时请求

]
