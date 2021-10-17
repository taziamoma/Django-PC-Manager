from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.context_processors import csrf
from django.urls import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from .models import *
import json, requests


# Create your views here.
class HomeView(ListView):
    template_name = 'index.html'
    queryset = Device.objects.all().order_by("-date")

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        devices = HomeView.queryset
        context['devices'] = devices

        return context


@csrf_exempt
def Api_System_Info(request):
    data = request.body.decode('utf-8')
    new_data = json.loads(data)

    saveget_attrs = {
        "name": new_data["PC_NAME"],
        "customer_name": new_data["NAME"],
        "customer_id": new_data["CUSTOMER_ID"],
        "asset_id": new_data["ASSET_ID"],
        "pc_user": new_data["USER"],
        "pc_cpu": new_data["CPU"],
        "pc_ram": new_data["RAM"],
        "pc_hd": new_data["HD"],
        "pc_os": new_data["PC_OS"],
        "pc_windows_key": new_data["WINDOWS_KEY"],
        "pc_gpu": new_data["GPU"],
        "motherboard_name": new_data["MB_NAME"],
        "motherboard_brand": new_data["MB_SERIAL"],
        "motherboard_serial": new_data["MB_SERIAL"],
        "pc_service_tag": new_data["PC_SERIAL"],
    }
    saving = Device.objects.create(**saveget_attrs)
    return HttpResponse(saveget_attrs)
