import random

from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from mocktest1.models import *
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# 打开项目列表
@login_required
def get_project_list(request):
    aaa = DB_project.objects.filter().all()
    return render(request, 'project_list.html', {"projects": aaa})


# 访问欢迎页面
@login_required
def welcome(request):
    return render(request, 'welcome.html')


# 删除项目路由
@login_required
def del_project(request, pid):
    DB_project.objects.filter(id=pid).delete()
    return HttpResponseRedirect('/project_list/')


# 复制项目路由
@login_required
def copy_project(request, pid):
    project = DB_project.objects.filter(id=pid).values()
    DB_project.objects.create(name=project.values()[0]['name'], creater=project.values()[0]['creater']).save()
    return HttpResponseRedirect('/project_list/')


# 请求登陆页面
def login(request):
    return render(request, 'login.html')


# 账号登录
def login_action(request):
    u_name = request.POST["in_username"]
    u_word = request.POST["in_password"]
    user = auth.authenticate(username=u_name, password=u_word)
    if user is not None:
        # 将登陆状态写到django服务端里面
        auth.login(request, user)
        # 登陆成功后将用户名添加到服务端session里面
        request.session['user'] = u_name
        return HttpResponseRedirect('/project_list/')
    else:
        return HttpResponseRedirect('/login/')


# 账号注册
def register_action(request):
    # 通知用户去邮箱获取验证码来激活账号
    # 验证失败了提示用户重新注册
    # 验证通过了就来添加用户，并通知前端注册成功
    u_name = request.POST["up_username"]
    u_word = request.POST["up_password"]
    u_email = request.POST["up_email"]
    try:
        user = User.objects.create_user(username=u_name, password=u_word, email=u_email)
        user.save()
        user = auth.authenticate(username=u_name, password=u_word)
        auth.login(request, user)
        return HttpResponseRedirect('/project_list/')
    except:
        return HttpResponseRedirect('/login/')


# 账号登出
@login_required
def logout(request):
    from django.contrib import auth
    auth.logout(request)
    return render(request, 'login.html')


# 发送邮箱验证码
def send_mail_code_action(request):
    email = request.GET['email']
    email_code = str(random.randint(1000, 9999))
    print(email_code)
    return HttpResponse("yes")
