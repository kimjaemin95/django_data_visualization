# -*- coding:utf-8 -*-
import json
import datetime
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .models import *
from collections import Counter  # 중복 수 체크

'''
http://pythonstudy.xyz/python/article/310-Django-%EB%AA%A8%EB%8D%B8-API
'''


def home(request):
    '''
    http://127.0.0.1:8000/vms/home/
    '''
    data = dict()
    def _common_code():
        common_code = VmsCommonCodeRef.objects.filter(type_id=2)
        common_code_dict = dict()
        for c in common_code:
            common_code_dict[str(c.code_id)] = c.code_name
        return common_code_dict

    def _device_model():
        models = VmsDeviceModel.objects.all()
        list_model_name = list()
        list_company = list()
        for m in models:
            list_model_name.append(m.model_name)
            list_company.append(m.company)
        return {'모델': dict(Counter(list_model_name)), '제조사': dict(Counter(list_company))}

    device_model = _device_model()
    common_code = _common_code()
    device = VmsDevice.objects.all().order_by('-sdc_upd_time')

    #   업데이트 시간 확인
    last_upt = device[0].sdc_upd_time + datetime.timedelta(hours=9)
    last_upt_str = last_upt.strftime('%Y-%m-%d %H:%M:%S')

    list_locations = list()
    list_stat = list()
    list_dev_type = list()
    list_company = list()
    for d in device:
        #   지역별 카메라 대수 확인
        try:
            location = d.dev_name.split(';')[2].split(' ')[0]
        except Exception as e:
            location = '데이터오류'
        list_locations.append(location)

        #   카메라 운영율 확인
        if int(d.dev_stat) == 0:
            stat = '비정상'
        else:
            stat = '정상'
        list_stat.append(stat)

        #   카메라 설치 유형 확인
        list_dev_type.append(common_code.get(str(d.dev_type)))
    stat_count = Counter(list_stat)

    data['행정동'] = dict(Counter(list_locations))
    data['설치유형'] = dict(Counter(list_dev_type))
    data['운영상태'] = {
        '전체수량': len(list_stat),
        '정상': stat_count.get('정상'),
        '비정상': stat_count.get('비정상'),
        '가동률': round(stat_count.get('정상') / len(list_stat) * 100 + 0, 2),
    }
    data['모델'] = device_model.get('모델')
    data['제조사'] = device_model.get('제조사')
    data['업데이트'] = last_upt_str
    return render(request, 'page/home.html', {'data':json.dumps(data)})

# Create your views here.
def vms_device(request):
    '''
    http://127.0.0.1:8000/vms/vms_device/
    '''
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
    return JsonResponse({'data': data})


def vms_device_analysis(request):
    '''
    http://127.0.0.1:8000/vms/vms_device_analysis/
    '''
    print(request.GET.get('test'))
    data = dict()
    try:
        def _common_code():
            common_code = VmsCommonCodeRef.objects.filter(type_id=2)
            common_code_dict = dict()
            for c in common_code:
                common_code_dict[str(c.code_id)] = c.code_name
            return common_code_dict

        def _device_model():
            models = VmsDeviceModel.objects.all()
            list_model_name = list()
            list_company = list()
            for m in models:
                list_model_name.append(m.model_name)
                list_company.append(m.company)
            return {'모델': dict(Counter(list_model_name)), '제조사': dict(Counter(list_company))}

        device_model = _device_model()
        common_code = _common_code()
        device = VmsDevice.objects.all().order_by('-sdc_upd_time')

        #   업데이트 시간 확인
        last_upt = device[0].sdc_upd_time + datetime.timedelta(hours=9)
        last_upt_str = last_upt.strftime('%Y-%m-%d %H:%M:%S')

        list_locations = list()
        list_stat = list()
        list_dev_type = list()
        list_company = list()
        for d in device:
            #   지역별 카메라 대수 확인
            try:
                location = d.dev_name.split(';')[2].split(' ')[0]
            except Exception as e:
                location = '데이터오류'
            list_locations.append(location)

            #   카메라 운영율 확인
            if int(d.dev_stat) == 0:
                stat = '비정상'
            else:
                stat = '정상'
            list_stat.append(stat)

            #   카메라 설치 유형 확인
            list_dev_type.append(common_code.get(str(d.dev_type)))
        stat_count = Counter(list_stat)

        data['행정동'] = dict(Counter(list_locations))
        data['설치유형'] = dict(Counter(list_dev_type))
        data['운영상태'] = {
            '전체수량': len(list_stat),
            '정상': stat_count.get('정상'),
            '비정상': stat_count.get('비정상'),
            '가동률': round(stat_count.get('정상') / len(list_stat) * 100 + 0, 2),
        }
        data['모델'] = device_model.get('모델')
        data['제조사'] = device_model.get('제조사')
        data['업데이트'] = last_upt_str
        return JsonResponse({'data': data}, json_dumps_params={'ensure_ascii': False}, status=200)
    except Exception as e:
        print(e)
        return HttpResponse(status=401)
