from django.db import models
import string
import random

def unique_code():
    length = 7

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Huddle.objects.all(roomID=code).count() == 0:
            break
    return code



class Huddle(models.Model):
    roomID = models.CharField(max_length=12, default='', unique=True)
    host = models.CharField(max_length=55, unique=True)
    guest_permit = models.BooleanField(null=False, default=False)
    skip_votes = models.IntegerField(null=False, default=1)
    created_at = models.DateTimeField(auto_now_add=True)
