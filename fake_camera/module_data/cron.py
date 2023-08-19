from django_cron import CronJobBase, Schedule
from .models import ModuleModel
import random
import logging
logger = logging.getLogger(__name__)
# new_data1 = ModuleModel(light_module_temperature=3,module_status="ON",internal_temp=internal_temp_rand,fan_status="ON")
# new_data1.save()

class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 1 # every 1 second
    RETRY_AFTER_FAILURE_MINS = 1
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS, retry_after_failure_mins=RETRY_AFTER_FAILURE_MINS)
    code = 'fake_camera.my_cron_job'    # a unique code

    def do(self):
        try:
            print(self.RUN_EVERY_MINS)
            print('started to update data!')
            light_module_rand = random.randint(1,4)
            internal_temp_rand = random.randint(1,5)
            module_on_off = random.choice(['ON', 'OFF'])
            fan_on_off = random.choice(['ON', 'OFF'])
            new_data = ModuleModel.objects.create(
                light_module_temperature=light_module_rand,
                module_status=module_on_off,internal_temp=internal_temp_rand,
                fan_status=fan_on_off
            )
        except Exception as e:
            logger.error('Error: %s', str(e), exc_info=True)
        logger.info('cron job finished')




        
