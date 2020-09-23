from django.contrib import admin
from .models import VmsDevice

# Register your models here.


class VmsDeviceAdmin(admin.ModelAdmin):
    list_display = ('id','dev_serial', 'dev_name', 'model_id', 'vms_id', 'dev_type', 'sdc_ins_time', 'sdc_upd_time')


admin.site.register(VmsDevice, VmsDeviceAdmin)