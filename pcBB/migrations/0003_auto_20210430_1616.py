# Generated by Django 3.2 on 2021-04-30 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pcBB', '0002_auto_20210430_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='motherboard_brand',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='device',
            name='motherboard_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='device',
            name='motherboard_serial',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='device',
            name='pc_cpu',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='device',
            name='pc_gpu',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='device',
            name='pc_hd',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='device',
            name='pc_os',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='device',
            name='pc_ram',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='device',
            name='pc_service_tag',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='device',
            name='pc_user',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='device',
            name='pc_windows_key',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
