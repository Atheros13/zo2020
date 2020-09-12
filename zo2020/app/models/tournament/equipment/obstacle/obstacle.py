from django.db import models

#from app.custom.model_fields  import CustomDistanceField

class ObstacleType(models.Model):

    ''' '''

    CHOICES_OBSTACLE = [
        ('Height', 'Height',
         'Width', 'Width',
         'Length', 'Length',
         'Weight', 'Weight')
        ]

    name = models.CharField(max_length=30, unique=True) # i.e. Hurdles
    obstacle = models.CharField(max_length=20, choices=CHOICES_OBSTACLE) # i.e. Height
    description = models.TextField(blank=True)

    def __str__(self):

        return self.name

class Obstacle(models.Model):

    ''' '''

    type = models.ForeignKey(ObstacleType, on_delete=models.CASCADE, related_name='obstacles')
    #value_distance = CustomDistanceField() # i.e. 1.2 m
    #value_weight = 

    def __str__(self):

        if self.type.obstacle in ['Height', 'Length', 'Width']:
            return '%s %s' % (self.value_distance, self.type.__str__())
        return self.type.__str__()
