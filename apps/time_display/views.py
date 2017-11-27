# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse,redirect
from time import gmtime,strftime
from django.utils.crypto import get_random_string
from models import *



# Create your views here.
def index(request):
    print strftime("%Y-%m-%d %H:%M:%S", gmtime())

    context = {
    "time": strftime("%Y-%m-%d %H:%M:%S", gmtime())
    }
    return render(request,'time_display/index.html',context)
