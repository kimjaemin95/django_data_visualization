# -*- coding:utf-8 -*-
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import *
from collections import Counter  # 중복 수 체크

'''
http://pythonstudy.xyz/python/article/310-Django-%EB%AA%A8%EB%8D%B8-API
'''


# Create your views here.
def vms_device(request):
    '''http://127.0.0.1:8000/vms/vms_device/'''
    device = VmsDevice.objects.all()
    # device = VmsDevice.objects.filter(sdc_upd_time__year='2020', sdc_upd_time__month='09', sdc_upd_time__day='22')
    data = list()

    for d in device:
        record = dict()
        record['id'] = d.id
        record['dev_serial'] = d.dev_serial
        record['dev_name'] = d.dev_name
        record['model_id'] = d.model_id
        record['vms_id'] = d.vms_id
        record['dev_type'] = d.dev_type
        record['dev_stat'] = d.dev_stat
        record['ins_time'] = d.ins_time
        record['mod_time'] = d.mod_time
        record['sdc_ins_time'] = d.sdc_ins_time
        record['sdc_upd_time'] = d.sdc_upd_time
        data.append(record)
    return JsonResponse({'data':data})



def vms_device_analysis(request):
    '''http://127.0.0.1:8000/vms/vms_device_analysis/'''
    device = VmsDevice.objects.all()
    locations_list = list()
    for d in device:
        try:
            location = d.dev_name.split(';')[2].split(' ')[0]
        except Exception as e:
            location = '데이터오류'
        locations_list.append(location)

    data = Counter(locations_list)
    return JsonResponse({'data':data}, content_type=u"application/json")
