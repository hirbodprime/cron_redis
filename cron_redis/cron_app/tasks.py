from celery import shared_task
from django.core.cache import cache
import requests

@shared_task
def my_celery_task():
    print("Running my Celery task")
    print('started to get data!')
    
    DATA_URL = 'http://127.0.0.1:8000/camera-data/'  # External endpoint that returns list of ids
    headers = {'user-agent': 'quickcheck/0.0.1'}
    
    response = requests.get(DATA_URL, headers=headers)
    status = response.status_code
    data = response.text
    
    if status == 200:
        # Store the fetched data in Redis cache
        cache.set('camera_data', data, timeout=3600)  # Cache for 1 hour
        print('Data stored in Redis cache')
    else:
        print(f'Failed to fetch data. Status code: {status}')
    
    print(status, data)
