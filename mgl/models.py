from django.db import models
from mgl.utils.images import resize_image

# Create your models here.

class GameList(models.Model):
    
    class Meta:
        verbose_name = 'Game list'
        verbose_name_plural = 'Game list'
    
    game_image = models.ImageField(upload_to='gameimages/', blank=True, null=True)
    game_name = models.CharField(max_length=250)
    hours_taken = models.CharField(blank=True, default='???', max_length=15)
    date_finished = models.CharField(blank=True, default='???', max_length=10)   
    about = models.TextField(blank=True)
    other = models.TextField(blank=True)
    
    def save (self, *args, **kwargs):
        super_save = super().save(*args, **kwargs)
        
        if self.game_image:
            resize_image(self.game_image, 125, 170, True, 70)
        
        return super_save
        