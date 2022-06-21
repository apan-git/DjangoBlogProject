#!/usr/bin/env python
# -*- coding: utf-8 -*-

# DateTime:2022/06/20 18:05:20

from django import views
from django.urls import path

from .views import index


urlpatterns = [
    path('', index, name='index')
]