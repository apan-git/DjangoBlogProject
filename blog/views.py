#!/usr/bin/env python
# -*- coding: utf-8 -*-

# DateTime:2022/06/20 18:05:57
from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    # return HttpResponse("欢迎访问我的博客")
    return render(
        request,
        'blog/index.html',
        context={
            "title": "博客首页",
            "welcome": "观影访问我的博客首页"
        }
    )


