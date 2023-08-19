# tasks.py

from celery import shared_task
import time
import requests


@shared_task
def my_celery_task():
    print("Running my Celery task")
    print('started to get data!')
    DATA_URL = 'http://127.0.0.1:8000/camera-data/' # external endpoint that returns list of ids
    headers = {'user-agent': 'quickcheck/0.0.1'}
    response = requests.get(DATA_URL, headers=headers)
    status = response.status_code
    data = response.text
    print(status,data)