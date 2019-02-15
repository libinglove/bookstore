from django.shortcuts import render, redirect, reverse
from users.models import Passport
import re


# Create your views here.
def register(request) :
    '''显示用户注册页面'''
    return render(request,'users/register.html')

def register_handle(request) :
    '''进行用户注册处理'''
    username = request.POST.get('user_name')
    password = request.POST.get('pwd')
    email = request.POST.get('email')

    # 进行数据校验
    if not all([username,password,email]) :
        return render(request,'users/register.html',{'errmsg':'参数不能为空！'})

    # 判断邮箱是否合法
    if not re.match(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email) :
        return render(request,'users/register.html',{'errmsg':'邮箱格式不正确！'})

    try:
        Passport.objects.add_one_passport(username=username,password=password,email=email)
    except Exception as e :
        print('e==',e)
        return render(request,'users/register.html',{'errmsg':'用户名已经存在'})

    return redirect(reverse('books:index'))
