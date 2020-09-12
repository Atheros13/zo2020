from django.db import models

#from zo.custom.customModels.customModelFields.customDistanceField import CustomDistanceField

class ApparatusType(models.Model):

    ''' '''

    name = models.CharField(max_length=30, unique=True) # Javelin
    description = models.TextField()

    def __str__(self):
        return self.name

class Apparatus(models.Model):

    ''' '''

    type = models.ForeignKey(ApparatusType, on_delete=models.CASCADE, related_name='apparatus')
    #value_distance = CustomDistanceField() # i.e. 1.2 m
    #value_weight = CustomWeightField() # i.e. 1.3 kg

    def __str__(self):

        return self.type.__str__()