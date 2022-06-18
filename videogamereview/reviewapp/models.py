from django.db import models
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Videogame(models.Model):
    GENRE_CHOICES = [
        ('Action', 'Action'),
        ('RPG', 'Role Playing Game'),
        ('Shooter', 'Shooter'),
        ('Sports', 'Sports'),
        ('Stealth', 'Stealth'),
        ('RTS', 'Real-Time Strategy'),
        ('Fighting', 'Fighting'),
        ('MMO', 'Massive Multiplayer Online'),
        ('Simulation', 'Simulation'),
        ('Horror', 'Horror'),
    ]
    Title=models.CharField(max_length=225)
    Developer=models.CharField(max_length=225)
    ReleaseDate=models.DateField()
    Genre=models.CharField(max_length=25, choices=GENRE_CHOICES, default='action')

    def __str__(self):
        return self.Title
    
    class Meta:
        db_table='videogame'

class Vgreview(models.Model):
    RATING_CHOICES = [
        (5,'5 Stars'),
        (4,'4 Stars'),
        (3,'3 Stars'),
        (2,'2 Stars'),
        (1,'1 Stars'),
    ]
    vgid=models.ForeignKey(Videogame, on_delete=models.CASCADE)
    Author=models.ForeignKey(User, on_delete=models.CASCADE)
    ReviewDate=models.DateField(auto_now_add=True)
    Title=models.CharField(max_length=225, default='')
    Rating=models.IntegerField(choices=RATING_CHOICES, default=5)
    Review=models.TextField()

    def __str__(self):
        return self.Title
    
    class Meta:
        db_table='vgreview'