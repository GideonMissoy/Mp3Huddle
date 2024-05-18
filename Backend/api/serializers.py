from rest_framework import serializers
from .models import *


class HuddleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Huddle
        fields = ('id', 'roomID', 'host', 'guest_permit', 'skip_votes', 'created_at')
