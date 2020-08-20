from django.db import models

# Create your models here.

class Production(models.Model):
    id = models.AutoField(primary_key=True)
    document_date = models.DateTimeField()
    posting_date = models.DateTimeField()
    plant = models.IntegerField(default=0)
    material = models.CharField(max_length=200)
    material_description = models.CharField(max_length=200)
    movement_type = models.CharField(max_length=10)
    cqe_1 = models.IntegerField()
    cqe_2 = models.IntegerField()
    que_1 = models.FloatField()
    que_2 = models.FloatField()
    ue = models.CharField(max_length=10)
    alc_1 =  models.FloatField()
    type = models.CharField(max_length=10)
    week = models.IntegerField()
    alc_2 = models.FloatField()
