from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from salary import salary


# Create your views here.

# index页面跳转 skill选项后端渲染
def index(request):
    skills = ['1.django', '2.scrapy/requests', '3.mysql', '4.mongodb', '5.linux/shell', '6.html/css/js',
              '7.http/tcp/ip', '8.sklearn/numpy', '9.selenium', '10.matplotlib', '11.git', '12.flask', '13.tordano',
              '14.ansible', '15.redis', '16.pandas']
    return render(request, 'info/index.html', {"skills": skills})


# 获取前端选择 调用预测函数 返回结果
def submit(request):
    city = str(request.GET.get('city'))
    exp = int(request.GET.get('experience'))
    edu = str(request.GET.get('education'))
    skill = int(request.GET.get('skill'))
    res = int(salary.wage_pred(city, exp, edu, skill)[0])
    return JsonResponse({'res': res})


# img页面跳转
def img(request):
    return render(request, 'info/img.html')
