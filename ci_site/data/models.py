from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from smart_selects.db_fields import ChainedForeignKey
from datetime import date
import calendar

my_date = date.today()

EVENT_CHOICES = (
    ('Warranty', 'Warranty'),
    ('Scrap', 'Scrap'),
    ('Rework', 'Rework'),
    ('Delay', 'Delay'),
    ('Reject', 'Reject')
)

PLANT_CHOICES = (
    ('Williams', 'Williams'),
    ('Cheyenne', 'Cheyenne'),
    ('Tomahawk', 'Tomahawk')
)

VALUESTREAM_CHOICES = (
    ('VS1', 'VS1'),
    ('VSO', 'VSO'),
    ('VSS', 'VSS'),
    ('VSRV', 'VSRV'),
    ('VSQ', 'VSQ')
)

PROCESS_STEP_CHOICES = (
    ('Interior', 'Interior'),
    ('Exterior', 'Exterior'),
    ('Frame', 'Frame'),
    ('Roof', 'Roof'),
    ('Floor', 'Floor'),
    ('Final', 'Final')
)


class Defect(models.Model):
    date_created = models.DateField(default=my_date, null=True)
    time_created = models.TimeField(auto_now_add=True, null=True)
    event = models.CharField(max_length=10, null=True, choices=EVENT_CHOICES)
    plant = models.CharField(max_length=10, null=True, choices=PLANT_CHOICES)
    value_stream = models.CharField(max_length=5, null=True, choices=VALUESTREAM_CHOICES)
    process_step = models.CharField(max_length=10, null=True, choices=PROCESS_STEP_CHOICES)
    day_of_week = models.CharField(max_length=10, default=calendar.day_name[my_date.weekday()])


class ChartDefect(Defect):
    class Meta:
        proxy = True


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    plant = models.CharField(max_length=10, choices=PLANT_CHOICES, null=True, blank=True)
    value_stream = models.CharField(max_length=5, choices=VALUESTREAM_CHOICES, null=True, blank=True)
    process_step = models.CharField(max_length=10, choices=PROCESS_STEP_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
