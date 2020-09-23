from django.db import models


# Create your models here.

class VmsDevice(models.Model):
    dev_serial = models.IntegerField(verbose_name='시리얼번호')
    dev_name = models.CharField(max_length=100, verbose_name='기기이름')
    model_id = models.IntegerField(verbose_name='모델아이디')
    vms_id = models.IntegerField(verbose_name='vms아이디')
    dev_type = models.CharField(max_length=45, verbose_name='기기타입')
    dev_stat = models.CharField(max_length=45, verbose_name='기기상태')
    ins_time = models.DateTimeField(verbose_name='데이터삽입시간')
    mod_time = models.DateTimeField(verbose_name='모드시간')
    sdc_ins_time = models.DateTimeField(verbose_name='INSERT시간')
    sdc_upd_time = models.DateTimeField(verbose_name='UPDATE시간')

    class Meta:
        db_table = 'vms_device'
        verbose_name = 'VMS DEVICE'
        verbose_name_plural = 'VMS DEVICE'

    def __str__(self):
        return self.dev_serial

