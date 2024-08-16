from django.contrib.auth.models import User
from django.db import models
from datetime import date

class Player(models.Model):
    positions = [
        ('GO', 'Goleiro'),
        ('ZG', 'Zagueiro'),
        ('LD', 'Lateral Direito'),
        ('LE', 'Lateral Esquerdo'),
        ('VOL', 'Volante'),
        ('MC', 'Meio Campo'),
        ('AT', 'Atacante'),
    ]
    leg = [
        ('D', 'Direita'),
        ('E', 'Esquerda'),
        ('A', 'Ambas')
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_born = models.DateField()
    position = models.CharField(max_length=3, choices=positions, default='GO')
    dominant_leg = models.CharField(max_length=1, choices=leg, default='')
    specialty = models.CharField(max_length=100)
    
    @property
    def idade(self):
        today = date.today()
        age = today.year - self.date_born.year
        if (today.month, today.day) < (self.date_born.month, self.date_born.day):
            age -= 1
        return age
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
