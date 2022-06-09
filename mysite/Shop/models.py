from django.db import models


class HardDrive(models.Model):
    kind_name = models.CharField(max_length=250)

    def __str__(self):
        return self.kind_name


class Design(models.Model):
    design_name = models.CharField(max_length=250)

    def __str__(self):
        return self.design_name


class GraphicsCard(models.Model):
    card_name = models.CharField(max_length=250)
    
    
    def __str__(self):
        return self.card_name


class PC(models.Model):
    design = models.ForeignKey(Design, on_delete=models.CASCADE)
    drive = models.ManyToManyField(HardDrive)
    card = models.ManyToManyField(GraphicsCard)
    pc_name = models.CharField(max_length=250)
    model = models.CharField(max_length=250)

    def __str__(self):
        return self.pc_name + '-' + self.model


