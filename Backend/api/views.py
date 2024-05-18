from django.shortcuts import render
from rest_framework import generics
from .serializers import HuddleSerializer
from .models import Huddle

#Create your views here
class HuddleView(generics.ListAPIView):
    queryset = Huddle.objects.all()
    serializer_class = HuddleSerializer