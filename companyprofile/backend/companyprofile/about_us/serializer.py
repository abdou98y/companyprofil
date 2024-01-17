from typing import Any
from rest_framework import serializers
from .models import *
from PIL import Image


class ImagesValidator():
    def __call__(self,value): 
        if not value :
            raise serializers.ValidationError("image field can't be impty")
        
        image = value
        max_size = 2 *1024*1024
        
        if image.size > max_size :
            raise serializers.ValidationError("image size can't exceed  2 MB")
        
        allowed_extension = ["jpeg","peg","png","webp"]
        ext = image.name.split('.')[-1].lower
        
        if ext not in  allowed_extension :
            raise serializers.ValidationError("image can  only be jpeg,peg,png,webp")
        if ext is not "webp":
            def convert_to_webp(image_path,output_path,quality=85):
                with Image.open(image_path)as imag:
                    image.save(output_path,"webp",quality=quality)

class PdfValidator():
    def __call__(self,value): 
        if not value :
            raise serializers.ValidationError("pdf field can't be impty")
        
        pdf = value
        max_size = 15 *1024*1024
        
        if pdf.size > max_size :
            raise serializers.ValidationError("pdf size can't exceed  15 MB")
        
        allowed_extension = "pdf"
        ext = pdf.name.split('.')[-1].lower
        
        if ext is not  allowed_extension :
            raise serializers.ValidationError("pdfs only can be uploaded")

class TitleDescriptionValidator():
    def __call__(self,value):
        if not value:
            raise serializers.ValidationError("can't be empty")

class NumberValidator():
    def __call__(self,value):
        if not value:
            raise serializers.ValidationError("can't be empty")
        if value == 0:
            raise serializers.ValidationError("can't be zero")
            



class about_us_serializer(serializers.ModelSerializer):
    header_first_title=serializers.CharField(validators=[TitleDescriptionValidator()])
    header_second_title=serializers.CharField(validators=[TitleDescriptionValidator()])
    header_banner=serializers.ImageField(validators=[ImagesValidator()])
    info_first_title = serializers.CharField(validators=[TitleDescriptionValidator()])
    info_second_title = serializers.CharField(validators=[TitleDescriptionValidator()])
    info_thierd_title = serializers.CharField(validators=[TitleDescriptionValidator()])
    info_first_discription=serializers.TextField(validators=[TitleDescriptionValidator()])
    info_second_discription=serializers.TextField(validators=[TitleDescriptionValidator()])
    pdf=serializers.FileField(validators=[NumberValidator()])
    statics_num = serializers.PositiveIntegerField(validators=[NumberValidator()])
    name= serializers.CharField(validators=[TitleDescriptionValidator()])
    number = serializers.PositiveIntegerField(validators=[NumberValidator()])
    vission_first_title=serializers.CharField(validators=[TitleDescriptionValidator()])
    vission_second_title=serializers.CharField(validators=[TitleDescriptionValidator()])
    vission_discription = serializers.TextField(validators=[TitleDescriptionValidator()])
    vission_banner = serializers.ImageField(validators=[ImagesValidator()])
    mission_first_title=serializers.CharField(validators=[TitleDescriptionValidator()])
    mission_second_title=serializers.CharField(validators=[TitleDescriptionValidator()])
    mission_discription = serializers.TextField(validators=[TitleDescriptionValidator()])
    mission_banner = serializers.ImageField(validators=[ImagesValidator()])
    core_value_title=serializers.CharField(validators=[TitleDescriptionValidator()])
    core_vlaues_num=serializers.PositiveIntegerField(validators=[NumberValidator()])
    value_title = serializers.CharField(validators=[TitleDescriptionValidator()])    
    value_description = serializers.TextField(validators=[TitleDescriptionValidator()])
    chairman_first_title = serializers.CharField(validators=[TitleDescriptionValidator()])    
    chairman_second_title = serializers.CharField(validators=[TitleDescriptionValidator()])    
    chairman_first_description = serializers.TextField(validators=[TitleDescriptionValidator()])
    chairman_image= serializers.ImageField(validators=[ImagesValidator()])
    chairman_second_description = serializers.TextField(validators=[TitleDescriptionValidator()])
    last_first_title= serializers.CharField(validators=[TitleDescriptionValidator()])
    last_second_title= serializers.CharField(validators=[TitleDescriptionValidator()])
    last_theird_title= serializers.CharField(validators=[TitleDescriptionValidator()])
    
    class HeaderSerializer:
        model = HeaderSection
        fields={
            "header_first_title",
            "header_second_title",
            "header_banner",
        }
        
    class InfoSerilaizer:
        model= InfoSection
        fields={
            "info_first_title", 
            "info_second_title",
            "info_thierd_title",
            'info_first_discription',
            "info_second_discription",
            "pdf",
            "statics_num",
            }
    
    class StaticsSerializer:
        model= StaticsSection
        fields={
            "name",
            "number", 
        }
    class VisionSerializer:
        model= VisionSection
        fields={
            " vission_first_title",
            'vission_second_title',
            "vission_discription",
            "vission_banner",
        }
    class MissionSerializer:
        model= MissionSection
        fields={
            "mission_first_title",
            "mission_second_title",
            "mission_discription",
            "mission_banner",
        }
    class CoreValueSectionSerializer:    
        model= CoreValueSection
        fields={
            "core_value_title",
            "core_vlaues_num", 
        }
    class CoreValuesSerializer:
        model= CoreValues
        fields={
            "value_title",
            "value_description",      
        }
    class ChairmanSerializer:
        model= ChairmanSection
        fields={
            'chairman_first_title',
            'chairman_second_title',
            "chairman_first_description",
            'chairman_image',
            'chairman_second_description',
        }
    class LastSerializer:
        model= LastSection
        fields={
            "last_first_title",
            "last_second_title",
            "last_theird_title",
        }