from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect
from mocktest1.models import *
from django.contrib import auth
from django.contrib.auth.models import User


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
    u_name = request.GET["username"]
    u_word = request.GET["password"]
    user = auth.authenticate(username=u_name, password=u_word)
    if user is not None:
        # 正确返回
        auth.login(request, user)
        # 登陆成功后将用户名添加到服务端session里面
        request.session['user'] = u_name
        return HttpResponse(0)
    else:
        return HttpResponse(1)
        # 提示账密错误


# 账号注册
def register_action(request):
    # 通知用户去邮箱获取验证码来激活账号
    # 验证失败了就天使用户重新注册
    # 验证通过了就来添加用户，并通知前端注册成功
    u_name = request.GET["username"]
    u_word = request.GET["password"]
    try:
        user = User.objects.create_user(username=u_name, password=u_word)
        user.save()
        return HttpResponse(0)
    except:
        return HttpResponse(1)


# 账号登出
@login_required
def logout(request):
    from django.contrib import auth
    auth.logout(request)
    return render(request, 'login.html')
