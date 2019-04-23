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
from django.conf.urls import url
from data.views import *

urlpatterns = [
    url(r'^test/$', get_test_data),
    url(r'^map/$', get_map_data),
    url(r'^hist/$', get_hist_data),
    url(r'^pie/$', get_pie_data),
    url(r'^line/$', get_line_data),
    url(r'^query/$', get_query_data),
    url(r'^knn/$', get_knn_data),
    url(r'^test.html$', get_test_page),
    url(r'^map.html$', get_map_page),
    url(r'^hist.html$', get_hist_page),
    url(r'^pie.html$', get_pie_page),
    url(r'^line.html$', get_line_page),
    url(r'^knn.html$', get_knn_page),
]
