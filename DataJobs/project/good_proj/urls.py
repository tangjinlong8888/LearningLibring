"""good_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

# from good import views
# from user import views
from good.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^good/', GoodList.as_view()),
    url(r'^index.html', order_index_page),
    # url(r'^index.html', views.order_index_zuire),
    # url(r'^tips.html',get_register_data),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^style/(?P<path>.*)$',serve),
    url(r'^gwfenxi',get_gwfenxi_page),
    url(r'^accountBind',get_accountBind_page),
    url(r'^auth',get_auth_page),
    url(r'^authSuccess',get_authSuccess_page),
    url(r'^autoFilterResumes',get_autoFilter_page),
    url(r'^bindstep1',get_bindstep1_page),
    url(r'^bindstep2',get_bindstep2_page),
    url(r'^bindstep3',get_bindstep3_page),
    url(r'^canInterviewResumes',get_canlnterview_page),
    url(r'^collections',get_collections_page),
    url(r'^companylist',get_companylist_page),
    url(r'^create',get_create_page),
    url(r'^delivery',get_delivery_page),
    url(r'^founder',get_founder_page),
    url(r'^haveRefuseResumes',get_haveRefuse_page),
    url(r'^index01',get_index01_page),
    url(r'^index02',get_index02_page),
    url(r'^index03',get_index03_page),
    url(r'^index04',get_index04_page),
    url(r'^index06',get_index06_page),
    url(r'^jianli',get_jianli_page),
    url(r'^jobdetail',get_jobdetail_page),
    url(r'^jobdetail1',get_jobdetail1_page),
    url(r'^mList',get_mList_page),
    url(r'^myhome',get_myhome_page),
    url(r'^positions',get_positions_page),
    url(r'^preview',get_preview_page),
    url(r'^reset',get_reset_page),
    url(r'^subscribe',get_subscribe_page),
    url(r'^subscribe01',get_subscribe01_page),
    url(r'^success',get_success_page),
    url(r'^tag',get_tag_page),
    url(r'^updatePassword',get_updatePwd_data),
    url(r'^tips.html',get_tips_page),
    url(r'^updatePwd.html',get_updatePwd_page),

    url(r'^list.html',order),
    url(r'^web_bj.html',order_web_bj),
    url(r'^web_sh.html',order_web_sh),
    url(r'^web_gz.html',order_web_gz),
    url(r'^web_sz.html', order_web_sz),
    url(r'^web_cd.html', order_web_cd),
    url(r'^web_hz.html', order_web_hz),
    url(r'^web_wh.html', order_web_wh),
    url(r'^web_nj.html', order_web_nj),
    url(r'^web_qt.html', order_web_qt),

    url(r'^javaall.html',order_javaall),
    url(r'^phpall.html', order_phpall),
    url(r'^androidall.html', order_androidall),
    url(r'^uiall.html', order_uiall),
    url(r'^pythonall.html', order_pythonall),
    url(r'^user/', include('user.urls')),
    url(r'^data/', include('data.urls')),
    # url(r'^', views.register_page),

]
urlpatterns += staticfiles_urlpatterns()