from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

# module_data = cache.get('module_data')
#     if not module_data:
#         module_data = Module.objects.first()
#         cache.set('module_data', module_data)


light_module_temperature_choices = (
    ('1',1),
    ('2',2),
    ('3',3),
    ('4',4),
)
internal_temp_choices = (
    ('1',1),
    ('2',2),
    ('3',3),
    ('4',4),
    ('5',5),
)
fan_status_choices = (
    ('ON','ON'),
    ('OFF','OFF'),
)
module_status_choices = (
    ('ON','ON'),
    ('OFF','OFF'),
)
class ModuleModel(models.Model):
    light_module_temperature = models.SmallIntegerField(choices=light_module_temperature_choices)
    module_status = models.CharField(max_length=3,choices=module_status_choices)
    bypass_history = models.CharField(max_length=500,null=True,blank=True)
    internal_temp = models.SmallIntegerField(choices=internal_temp_choices)
    fan_status = models.CharField(max_length=3,choices=fan_status_choices)

@receiver(pre_save, sender=ModuleModel)
def update_bypass_history(sender, instance, **kwargs):
    if instance.pk:  # Check if the instance already exists in the database
        old_instance = sender.objects.get(pk=instance.pk)
        if old_instance.module_status != instance.module_status:
            history_entry = f"{instance.module_status} at {instance.pk}\n"
            instance.bypass_history = history_entry + instance.bypass_history
