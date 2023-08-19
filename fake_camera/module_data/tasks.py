# tasks.py

from celery import shared_task
import time
from .models import ModuleModel
import random


@shared_task
def my_celery_task():
    print("Running my Celery task")
    light_module_rand = random.randint(1,4)
    internal_temp_rand = random.randint(1,5)
    module_on_off = random.choice(['ON', 'OFF'])
    fan_on_off = random.choice(['ON', 'OFF'])
    new_data = ModuleModel.objects.create(
        light_module_temperature=light_module_rand,
        module_status=module_on_off,internal_temp=internal_temp_rand,
        fan_status=fan_on_off
    )
