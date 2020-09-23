from django.contrib import admin
from .models import VmsDevice

# Register your models here.


class VmsDeviceAdmin(admin.ModelAdmin):
    pass
    # list_display = ('id','username', 'password')

admin.site.register(VmsDevice, VmsDeviceAdmin)