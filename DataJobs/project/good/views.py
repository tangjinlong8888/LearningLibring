from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
import pandas as pd
from good.models import Good
from good.serializers import GoodSerializers
from rest_framework import mixins, status
from good import dq_user
import pymysql
from django.contrib.auth.hashers import make_password,check_password
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/spider')
# engine = create_engine('mysql+pymysql://admin:123456@192.168.2.104:3306/zl_db')



#将网页添加到url中显示
def get_gwfenxi_page(request):
    return render(request, 'gwfenxi.html', {'order': dq_user.dq_user()})
def get_accountBind_page(request):
    sql = 'select email from dq_user'
    df = pd.read_sql_query(sql,engine)
    m_data = (list(df['email']))[0]
    sql1 = 'select qq from users where email="{}"'.format(m_data)
    df1 = pd.read_sql_query(sql1, engine)
    m_data1 = (list(df1['qq']))[0]
    return render(request,'accountBind.html',{'order': dq_user.dq_user(),'order1':m_data,'order2':m_data1})
def get_auth_page(request):
    return render(request,'auth.html',{'order': dq_user.dq_user()})
def get_authSuccess_page(request):
    return render(request,'authSuccess.html',{'order': dq_user.dq_user()})
def get_autoFilter_page(request):
    return render(request,'autoFilterResumes.html',{'order': dq_user.dq_user()})
def get_bindstep1_page(request):
    return render(request,'bindstep1.html',{'order': dq_user.dq_user()})
def get_bindstep2_page(request):
    return render(request,'bindstep2.html',{'order': dq_user.dq_user()})
def get_bindstep3_page(request):
    return render(request,'bindstep3.html',{'order': dq_user.dq_user()})
def get_canlnterview_page(request):
    return render(request,'canInterviewResumes.html',{'order': dq_user.dq_user()})
def get_collections_page(request):
    return render(request,'collections.html',{'order': dq_user.dq_user()})
def get_companylist_page(request):
    return render(request,'companylist.html',{'order': dq_user.dq_user()})
def get_create_page(request):
    return render(request,'create.html',{'order': dq_user.dq_user()})
def get_delivery_page(request):
    return render(request,'delivery.html',{'order': dq_user.dq_user()})
def get_founder_page(request):
    return render(request,'founder.html',{'order': dq_user.dq_user()})
def get_haveRefuse_page(request):
    return render(request,'haveRefuseResumes.html',{'order': dq_user.dq_user()})
def get_index01_page(request):
    return render(request,'index01.html',{'order': dq_user.dq_user()})
def get_index02_page(request):
    return render(request,'index02.html',{'order': dq_user.dq_user()})
def get_index03_page(request):
    return render(request,'index03.html',{'order': dq_user.dq_user()})
def get_index04_page(request):
    return render(request,'index04.html',{'order': dq_user.dq_user()})
def get_index06_page(request):
    return render(request,'index06.html',{'order': dq_user.dq_user()})
def get_jianli_page(request):
    return render(request,'jianli.html',{'order': dq_user.dq_user()})
def get_jobdetail_page(request):
    return render(request,'jobdetail.html',{'order': dq_user.dq_user()})
def get_jobdetail1_page(request):
    return render(request,'jobdetail1.html',{'order': dq_user.dq_user()})
def get_list_page(request):
    return render(request,'list.html',{'order': dq_user.dq_user()})
def get_login_page(request):
    return render(request,'login.html',{'order': dq_user.dq_user()})
def get_mList_page(request):
    return render(request,'mList.html',{'order': dq_user.dq_user()})
def get_myhome_page(request):
    return render(request,'myhome.html',{'order': dq_user.dq_user()})
def get_positions_page(request):
    return render(request,'positions.html',{'order': dq_user.dq_user()})
def get_preview_page(request):
    return render(request,'preview.html',{'order': dq_user.dq_user()})
def get_reset_page(request):
    return render(request,'reset.html',{'order': dq_user.dq_user()})
def get_subscribe_page(request):
    return render(request,'subscribe.html',{'order': dq_user.dq_user()})
def get_subscribe01_page(request):
    return render(request,'subscribe01.html',{'order': dq_user.dq_user()})
def get_success_page(request):
    return render(request,'success.html',{'order': dq_user.dq_user()})
def get_tag_page(request):
    return render(request,'tag.html',{'order': dq_user.dq_user()})
def get_updatePwd_page(request):
    sql = 'select email from dq_user'
    df = pd.read_sql_query(sql, engine)
    m_data = (list(df['email']))[0]
    return render(request,'updatePwd.html',{'order': dq_user.dq_user(),'order1':m_data})
    # return render(request,'updatePwd.html')
def get_updatePwd_data(request):

    oldpwd = request.POST.get('oldPassword', '')
    newpwd = request.POST.get('newPassword', '')
    sql = 'select email from dq_user '
    df = pd.read_sql_query(sql, engine)
    m_email = (list(df['email']))[0]
    result = {'success': 0}
    sql2 = 'select password from users where email="{}"'.format(m_email)
    df = pd.read_sql_query(sql2, engine)
    m_data = list(df['password'])[0]
    newpwd = make_password(newpwd)
    if check_password(oldpwd,m_data):
        sql1 = 'update users set password="{}" where email="{}"'.format(newpwd, m_email)
        print(sql1)
        try:
            pd.read_sql_query(sql1, engine)
        except:
            pass
        result['success'] = 1
    else:
        result['msg'] = '密码不正确，请重试！'
    print(result)
    return JsonResponse(result)
def get_tips_page(request):
    return render(request,'tips.html')

class GoodList(APIView):
    """
    List all snippets, or create a new snippet.
    """

    def get(self, request, format=None):
        goods = Good.objects.all()
        serializer = GoodSerializers(goods, many=True)
        data = dict()
        data['errcode'] = 0
        data['results'] = serializer.data
        return Response(data)
        # return redirect(get_index_page)
        # return render(request,'index.html',data)

    def post(self, request, format=None):
        print(request.data)
        serializer = GoodSerializers(data=request.data)
        print(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




#获取数据库的数据
def get_data(sql):
    conn = pymysql.connect('127.0.0.1','root','123456','spider',3306)
    # conn = pymysql.connect('192.168.2.104','admin','123456','zl_db',3306)
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    #搜取所有结果
    results = cur.fetchall()
    cur.close()
    conn.close()
    return results
#向页面输出数据
def order(request):
    sql = 'select * from weball'
    m_data = get_data(sql)
    paginator = Paginator(m_data,50)
    page = request.GET.get('page')
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)
    return render(request,'list.html',{'order':customer,'order1': dq_user.dq_user()})
def order_web_bj(request):
    sql = 'select * from web where city="北京"'
    # sql1 = 'select * from web where city="北京" and (money like "%-2K" or money ="薪资面议")'
    # sql2 = 'select * from web where city="北京" and (money like "%-5K" or money ="薪资面议")'
    m_data = get_data(sql)
    paginator = Paginator(m_data, 50)
    page = request.GET.get('page')
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)
    return render(request,'web_bj.html',{'order':customer,'order1': dq_user.dq_user()})
def order_web_sh(request):
    sql = 'select * from web where city="上海"'
    m_data = get_data(sql)
    paginator = Paginator(m_data, 60)
    page = request.GET.get('page')
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)
    return render(request,'web_sh.html',{'order':customer,'order1': dq_user.dq_user()})
def order_web_gz(request):
    sql = 'select * from web where city="广州"'
    m_data = get_data(sql)
    paginator = Paginator(m_data, 60)
    page = request.GET.get('page')
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)
    return render(request,'web_gz.html',{'order':customer,'order1': dq_user.dq_user()})
def order_web_sz(request):
    sql = 'select * from web where city="深圳"'
    m_data = get_data(sql)
    paginator = Paginator(m_data, 60)
    page = request.GET.get('page')
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)
    return render(request,'web_sz.html',{'order':customer,'order1': dq_user.dq_user()})
def order_web_cd(request):
    sql = 'select * from web where city="成都"'
    m_data = get_data(sql)
    paginator = Paginator(m_data, 60)
    page = request.GET.get('page')
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)
    return render(request,'web_cd.html',{'order':customer,'order1': dq_user.dq_user()})
def order_web_hz(request):
    sql = 'select * from web where city="杭州"'
    m_data = get_data(sql)
    paginator = Paginator(m_data, 60)
    page = request.GET.get('page')
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)
    return render(request,'web_hz.html',{'order':customer,'order1': dq_user.dq_user()})
def order_web_wh(request):
    sql = 'select * from web where city="武汉"'
    m_data = get_data(sql)
    paginator = Paginator(m_data, 60)
    page = request.GET.get('page')
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)
    return render(request,'web_wh.html',{'order':customer,'order1': dq_user.dq_user()})
def order_web_nj(request):
    sql = 'select * from web where city="南京"'
    m_data = get_data(sql)
    paginator = Paginator(m_data, 60)
    page = request.GET.get('page')
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)
    return render(request,'web_nj.html',{'order':customer,'order1': dq_user.dq_user()})
def order_web_qt(request):

    sql = 'select * from web where city!="南京" and city!="武汉"and city!="杭州"and city!="成都"and city!="深圳"and city!="广州"and city!="上海"and city!="北京"'
    m_data = get_data(sql)
    paginator = Paginator(m_data, 60)
    page = request.GET.get('page')
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)
    return render(request,'web_qt.html',{'order':customer,'order1': dq_user.dq_user()})
def order_index_page(request):
    sql = 'select * from zl_computer limit 10'
    sql2 = 'select * from zl_fangdc limit 10'
    sql3 = 'select * from zl_xingzheng limit 10'
    sql4 = 'select * from zl_wuliu limit 10'
    sql5 = 'select * from zl_jinrong limit 10'
    data = get_data(sql)
    data2 = get_data(sql2)
    data3 = get_data(sql3)
    data4 = get_data(sql4)
    data5 = get_data(sql5)
    m_data = data+data2+data3+data4+data5
    sql6 = 'select * from zl_computer where timestate="最新" limit 10'
    sql7 = 'select * from zl_jinrong where timestate="最新" limit 10'
    sql8 = 'select * from zl_jiaoyu where timestate="最新" limit 10'
    sql9 = 'select * from zl_fangdc where timestate="最新" limit 10'
    sql10 = 'select * from zl_fuwu where timestate="最新" limit 10'
    data = get_data(sql6)
    data2 = get_data(sql7)
    data3 = get_data(sql8)
    data4 = get_data(sql9)
    data5 = get_data(sql10)
    m_data1 = data + data2 + data3 + data4 + data5
    return render(request,'index.html',{'order2': dq_user.dq_user(),'order':m_data,'order1':m_data1})

def order_javaall(request):
    sql = 'select * from javaall'
    m_data = get_data(sql)
    paginator = Paginator(m_data, 60)
    page = request.GET.get('page')
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)
    return render(request,'javaall.html',{'order':customer,'order1': dq_user.dq_user()})
def order_phpall(request):
    sql = 'select * from phpall'
    m_data = get_data(sql)
    paginator = Paginator(m_data, 60)
    page = request.GET.get('page')
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)
    return render(request,'phpall.html',{'order':customer,'order1': dq_user.dq_user()})
def order_androidall(request):
    sql = 'select * from androidall'
    m_data = get_data(sql)
    paginator = Paginator(m_data, 60)
    page = request.GET.get('page')
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)
    return render(request,'androidall.html',{'order':customer,'order1': dq_user.dq_user()})
def order_uiall(request):
    sql = 'select * from uiall'
    m_data = get_data(sql)
    paginator = Paginator(m_data, 60)
    page = request.GET.get('page')
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)
    return render(request,'uiall.html',{'order':customer,'order1': dq_user.dq_user()})
def order_pythonall(request):
    sql = 'select * from pythonall'
    m_data = get_data(sql)
    paginator = Paginator(m_data, 60)
    page = request.GET.get('page')
    try:
        customer = paginator.page(page)
    except PageNotAnInteger:
        customer = paginator.page(1)
    except EmptyPage:
        customer = paginator.page(paginator.num_pages)
    return render(request,'pythonall.html',{'order':customer,'order1': dq_user.dq_user()})