# -*- coding:utf-8 -*-
from django.db import models


class Phone(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=150)
    price = models.IntegerField()
    release_date = models.CharField(max_length=15)
    lte_exists = models.CharField(max_length=5)
    slug = models.SlugField(max_length=50)
