from rest_framework import serializers
from .models import my_data




class my_data_serializer(serializers.Serializer):
    class meta :
        model=my_data
        feilds="__all__"