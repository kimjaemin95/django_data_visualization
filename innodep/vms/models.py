from django.db import models


# Create your models here.

class VmsDevice(models.Model):
    dev_serial = models.IntegerField(verbose_name='시리얼번호')
    dev_name = models.CharField(max_length=100, verbose_name='기기이름')
    model_id = models.IntegerField(verbose_name='모델아이디', blank=True, null=True)
    vms_id = models.IntegerField(verbose_name='vms아이디', blank=True, null=True)
    dev_type = models.CharField(max_length=45, verbose_name='기기타입', blank=True, null=True)
    dev_stat = models.CharField(max_length=45, verbose_name='기기상태', blank=True, null=True)
    longitude = models.CharField(max_length=45, verbose_name='경도', blank=True, null=True)
    latitude = models.CharField(max_length=45, verbose_name='위도', blank=True, null=True)
    ins_time = models.DateTimeField(verbose_name='데이터삽입시간', blank=True, null=True)
    mod_time = models.DateTimeField(verbose_name='모드시간', blank=True, null=True)
    sdc_ins_time = models.DateTimeField(verbose_name='INSERT시간', blank=True, null=True)
    sdc_upd_time = models.DateTimeField(verbose_name='UPDATE시간', blank=True, null=True)

    class Meta:
        db_table = 'vms_device'
        verbose_name = 'VMS DEVICE'
        verbose_name_plural = 'VMS DEVICE'

    def __str__(self):
        return self.dev_serial


class VmsDeviceModel(models.Model):
    model_id = models.IntegerField(verbose_name='모델아이디')
    model_name = models.CharField(max_length=45, verbose_name='모델이름')
    company = models.CharField(max_length=45, verbose_name='회사', blank=True, null=True)
    model_driver = models.CharField(max_length=45, verbose_name='모델드라이버', blank=True, null=True)
    ins_time = models.DateTimeField(verbose_name='데이터삽입시간', blank=True, null=True)
    mod_time = models.DateTimeField(verbose_name='모드시간', blank=True, null=True)
    sdc_ins_time = models.DateTimeField(verbose_name='INSERT시간', blank=True, null=True)
    sdc_upd_time = models.DateTimeField(verbose_name='UPDATE시간', blank=True, null=True)

    class Meta:
        db_table = 'vms_device_model'
        verbose_name = 'VMS DEVICE MODEL'
        verbose_name_plural = 'VMS DEVICE MODEL'

    def __str__(self):
        return self.model_name


class VmsCommonCodeRef(models.Model):
    type_id = models.IntegerField(verbose_name='타입아이디')
    code_id = models.IntegerField(verbose_name='코드아이디')
    code_name = models.CharField(max_length=50, verbose_name='코드이름')

    class Meta:
        db_table = 'vms_common_code_ref'
        verbose_name = 'VMS COMMON CODE REF'
        verbose_name_plural = 'VMS COMMON CODE REF'

    def __str__(self):
        return self.code_name