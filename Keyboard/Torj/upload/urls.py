# -*- coding:utf-8 -*-
from django.conf.urls import url

from upload import views

urlpatterns = [
    url(r'upload/', views.upload)
]