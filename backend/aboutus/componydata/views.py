from django.shortcuts import render
from .models import my_data
from .serializers import my_data_serializer
from rest_framework import generics
from rest_framework.response import Response





# Create your views here.




class MydataDetailAPIView(generics.RetrieveAPIView):
    queryset = my_data.objects.all()
    serializer_class = my_data_serializer
    lookup_field="pk"

my_data_view = MydataDetailAPIView

class MydataUpdateAPIView(generics.UpdateAPIView):
    queryset = my_data.objects.all()
    serializer_class = my_data_serializer
    lookup_field="pk"
    def perform_update(self, serializer):
        return super().perform_update(serializer)