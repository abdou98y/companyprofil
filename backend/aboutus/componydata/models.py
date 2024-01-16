from django.db import models

# Create your models here.



class my_data(models.Model):
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    first_title=models.CharField(max_length=10000)
    second_title=models.CharField(max_length=10000)
    thierd_title=models.CharField(max_length=10000)
    fourth_title=models.CharField(max_length=10000)
    fifth_title=models.CharField(max_length=10000)
    first_banar=models.ImageField(upload_to='banners/', blank=True, null=True)
    pj_num= models.IntegerField()
    cl_num= models.IntegerField()
    unts_num=models.IntegerField()
    paragraph1=models.TextField()
    paragraph2=models.TextField()
    pdf=models.FileField()
    mson=models.CharField(max_length=10000)
    msn1=models.CharField(max_length=10000)
    msn_par1=models.TextField()
    second_banar=models.ImageField(upload_to='banners/', blank=True, null=True)
    mson2=models.CharField(max_length=10000)
    msn2=models.CharField(max_length=10000)
    msn_par2=models.TextField()
    theird_banar=models.ImageField(upload_to='banners/', blank=True, null=True)
    cr_value=models.CharField(max_length=10000)
    cr_sent1=models.CharField(max_length=10000)
    cr_par1=models.TextField()
    cr_sent2=models.CharField(max_length=10000)
    cr_par2=models.TextField()
    cr_sent3=models.CharField(max_length=10000)
    cr_par3=models.TextField()
    cr_sent4=models.CharField(max_length=10000)
    cr_par4=models.TextField()
    cr_sent5=models.CharField(max_length=10000)
    cr_par5=models.TextField()
    chierman=models.CharField(max_length=10000)
    chierman_title=models.CharField(max_length=10000)
    chierman_paragraph=models.TextField()
    chierman_img=models.ImageField(upload_to='imgs/', blank=True, null=True)
    chierman_paragraph2=models.TextField()
    last_statment=models.CharField(max_length=10000)
    last_statment2=models.CharField(max_length=10000)
    last_statment3=models.CharField(max_length=10000)
    
    def __str__(self):
        return self
    
