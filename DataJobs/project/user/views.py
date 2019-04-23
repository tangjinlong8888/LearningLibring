from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.hashers import make_password,check_password
from good.views import get_data
# Create your views here.
from sqlalchemy import create_engine
import pymysql
from good import dq_user
import pandas as pd
engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/spider')
def register(request):
    email = request.POST.get('email', 'shujuJobs@sjjs.com')
    password = make_password(request.POST.get('password', '123456'))
    name = request.POST.get('name', 'shujuJobs')
    sex = request.POST.get('sex', '男')
    phone = request.POST.get('phone', '18001010101')
    qq_number = request.POST.get('qq', '1234567890')
    xueli = request.POST.get('xueli', '本科')
    birthday = request.POST.get('birthday', '2000.01.01')
    shool = request.POST.get('shool', '四川大学')
    jiguan = request.POST.get('jiguan', '四川')

    sql = 'select email from users where email="{}"'.format(email)
    sql1 = 'select qq from users where qq="{}"'.format(qq_number)
    df = pd.read_sql_query(sql, engine)
    df1 = pd.read_sql_query(sql1, engine)
    result = {'success': 0}
    if len(list(df['email'])) > 0:
        result['msg'] = '邮箱已存在，请重试！'
    if len(list(df1['qq'])) > 0:
        result['msg1'] = 'qq已存在，请重试！'
    else:
        sql2 = 'insert into users(qq,email,password,name,sex,phone,xueli,birthday,shool,jiguan) \
                              values("{}","{}","{}","{}","{}","{}","{}","{}","{}","{}")'.format(
            qq_number, email, password, name, sex, phone, xueli, birthday, shool, jiguan)
        get_data(sql2)
        result['success'] = 1
    return JsonResponse(result)

def login(request):

    email = request.POST.get('email','123456@qq.com')
    pwd = request.POST.get('password','123456')
    print(email,pwd)
    sql = 'select email,password from users where email="{}"'.format(email)
    df = pd.read_sql_query(sql,engine)
    result = {'success': 0}
    if len(list(df['password'])) > 0:
        password = list(df['password'])[0]
    else:
        password = ''
    print(password)
    if password == '':
       result['msg'] = '账号不存在，请先注册！'
    elif check_password(pwd,password):
        try:
            sql2 = 'insert into dq_user(email) values ("{}")'.format(email)
            pd.read_sql_query(sql2,engine)
        except:
            pass
        result['success'] = 1
        result['content'] = '/index'

    else:
        result['msg'] = '密码不正确，请重试！'
    print(result)
    return JsonResponse(result)

def register_page(request):
    return render(request,'register.html')

def login_page(request):
    return render(request,'login.html')

