from django.contrib import admin
from .models import Board


# Register your models here.


class BoardAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'registered_date')

admin.site.register(Board, BoardAdmin)