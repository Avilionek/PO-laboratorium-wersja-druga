from django.db import models

class PC(models.Model):
    company = models.CharField(max_length=250)
    pc_name = models.CharField(max_length=250)
    model = models.CharField(max_length=250)
    pc_logo = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('date published')

class HardDrive(models.Model):
    pc = models.ForeignKey(PC, on_delete=models.CASCADE)
    drive_name = models.CharField(max_length=250)


class GraphicsCard(models.Model):
    card = models.ForeignKey(PC, on_delete=models.CASCADE)
    card_name = models.CharField(max_length=250)


