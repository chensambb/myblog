# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site

# Create your models here.
class Tag(models.Model):
    tag_name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.tag_name



class Article(models.Model) :
    title = models.CharField(max_length = 100)
    category = models.CharField(max_length = 50, blank = True) 
    date_time = models.DateTimeField(auto_now_add = True) 
    content = models.TextField(blank = True, null = True)

    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id':self.id})
        return "http://192.168.7.10:81%s" % path

    def __str__(self) :
        return self.title

    class Meta:
        ordering = ['-date_time']
