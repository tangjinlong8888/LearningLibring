# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.files import File
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


# Create your views here.
def save_file(filename, file):
    assert isinstance(file, File)
    with open("./keyboard/" + filename, "w") as fp:
        for chunk in file.chunks():
            fp.write(chunk)


def upload(request, *args, **kwargs):
    assert isinstance(request, HttpRequest)
    for file_name in request.FILES:
        save_file(file_name, request.FILES[file_name])

    return HttpResponse("")
