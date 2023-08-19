from django_cron import CronJobBase, Schedule
import requests


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 5 # every 5 minutes
    RETRY_AFTER_FAILURE_MINS = 1
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS, retry_after_failure_mins=RETRY_AFTER_FAILURE_MINS)
    code = 'cron_app.my_cron_job'    # a unique code

    def do(self):
        print('started to get data!')
        DATA_URL = '127.0.0.1:8080/camera-data/' # external endpoint that returns list of ids
        headers = {'user-agent': 'quickcheck/0.0.1'}
        response = requests.get(DATA_URL, headers=headers)
        status = response.status_code
        data = response.text
        print(status,data)

# def get_fake_data():
#     r = requests.get('127.0.0.1:8080/camera-data/')
#     status = r.status_code
#     data = r.text
#     print(status,data)