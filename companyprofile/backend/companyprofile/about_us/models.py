from django.db import models

# Create your models here.


class HeaderSection(models.Model):
    header_first_title=models.CharField(max_length=250)
    header_second_title=models.CharField(max_length=250)
    header_banner=models.ImageField()
    
class InfoSection(models.Model):
    info_first_title = models.CharField(max_length=250)
    info_second_title = models.CharField(max_length=250)
    info_thierd_title = models.CharField(max_length=250)
    info_first_discription=models.TextField()
    info_second_discription=models.TextField()
    pdf=models.FileField()
    statics_num = models.PositiveIntegerField()
    def create_statics(self):
        for i in range (self.statics_num):
            StaticsSection.objects.create(name=f"name{i}",number=i)

class StaticsSection(models.Model):
    name= models.CharField(max_length=250)
    number = models.PositiveIntegerField(max_length=20)
    
class VisionSection(models.Model):
    vission_first_title=models.CharField(max_length=250)
    vission_second_title=models.CharField(max_length=250)
    vission_discription = models.TextField()
    vission_banner = models.ImageField()

class MissionSection(models.Model):
    mission_first_title=models.CharField(max_length=250)
    mission_second_title=models.CharField(max_length=250)
    mission_discription = models.TextField()
    mission_banner = models.ImageField()

class CoreValueSection(models.Model):
    core_value_title=models.CharField(max_length=250)
    core_vlaues_num=models.PositiveIntegerField()
    def create_core_values(self):
        for i in range (self.core_vlaues_num):
            CoreValues.objects.Create(value_title=f"title{i}",value_description=f"discription{i}")
    
class CoreValues(models.Model):
    value_title = models.CharField(max_length=250)    
    value_description = models.TextField()
    
class ChairmanSection(models.Model):
    chairman_first_title = models.CharField(max_length=250)    
    chairman_second_title = models.CharField(max_length=250)    
    chairman_first_description = models.TextField()
    chairman_image= models.ImageField()
    chairman_second_description = models.TextField()
    
class LastSection(models.Model):
    last_first_title= models.CharField(max_length=250)
    last_second_title= models.CharField(max_length=250)
    last_theird_title= models.CharField(max_length=250)
    
    