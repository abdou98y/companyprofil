from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework import generics


# Create your views here.

class CombinedListView(generics.ListAPIView):
    serializer_class = about_us_serializer
    def get_queryset(self):
        # Retrieve data from all models
        header_data = HeaderSection.objects.all()
        info_data = InfoSection.objects.all()
        statics_data = StaticsSection.objects.all()
        vision_data = VisionSection.objects.all()
        mission_data = MissionSection.objects.all()
        core_value_data = CoreValueSection.objects.all()
        chairman_data = ChairmanSection.objects.all()
        last_data = LastSection.objects.all()

        # Combine data into a single queryset
        combined_data = (
            header_data | info_data | statics_data | vision_data | mission_data |
            core_value_data | chairman_data | last_data
        )
        # queryset = combined_data
        return combined_data
    
# class CombinedSerializer(serializers.Serializer):
#     header_data = HeaderSerializer(many=True)
#     info_data = InfoSerializer(many=True)
#     statics_data = StaticsSerializer(many=True)
#     vision_data = VisionSerializer(many=True)
#     mission_data = MissionSerializer(many=True)
#     core_value_data = CoreValueSerializer(many=True)
#     chairman_data = ChairmanSerializer(many=True)
#     last_data = LastSerializer(many=True)