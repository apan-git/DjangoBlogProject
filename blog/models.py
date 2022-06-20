#!/usr/bin/env python
# -*- coding: utf-8 -*-

# DateTime:2022/06/20 17:25:15


from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    """
    类别
    """
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name

class Tag(models.Model):
    """
    标签
    """
    name = models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.name

class Post(models.Model):
    """
    文章
    """
    # 文章标题
    title = models.CharField(max_length=70)

    # 文章内容
    body = models.TextField()

    # 创建时间
    created_time = models.DateTimeField()
    # 修改时间
    modified_time = models.DateTimeField()

    # 文章摘要 可以为空
    excerpt = models.CharField(max_length=200, blank=True) 

    # 分类，外键关联
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # 标签 多对多关联
    tags = models.ManyToManyField(Tag, blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.title


