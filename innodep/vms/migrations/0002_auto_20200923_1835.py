# Generated by Django 2.1.15 on 2020-09-23 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vms', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='VmsCommonCodeRef2',
            new_name='VmsCommonCodeRef',
        ),
        migrations.AlterModelTable(
            name='vmscommoncoderef',
            table='vms_common_code_ref',
        ),
    ]
