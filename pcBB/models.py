from django.db import models
from django.contrib.auth.models import User
import decimal

# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=255, blank=True)
    customer_name = models.CharField(max_length=255, blank=True)
    customer_id = models.IntegerField(default=0)
    asset_id = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    pc_user = models.CharField(max_length=255, blank=True)
    pc_cpu = models.CharField(max_length=255, blank=True)
    pc_ram = models.CharField(max_length=255, blank=True)
    pc_hd = models.CharField(max_length=255, blank=True)
    pc_os = models.CharField(max_length=255, blank=True)
    pc_windows_key = models.CharField(max_length=255, blank=True, null=True)
    pc_gpu = models.CharField(max_length=255, blank=True)
    motherboard_name = models.CharField(max_length=255, blank=True)
    motherboard_brand = models.CharField(max_length=255, blank=True)
    motherboard_serial = models.CharField(max_length=255, blank=True)
    pc_service_tag = models.CharField(max_length=255, blank=True)


    #user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
