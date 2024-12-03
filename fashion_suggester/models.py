# fashion_suggester/models.py

from django.db import models
from django.contrib.auth.models import User

class UserPrediction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comfort_level = models.IntegerField()
    fit_sizing_level = models.IntegerField()
    preferred_piece = models.CharField(max_length=100)
    design_style = models.CharField(max_length=50)
    material_quality = models.CharField(max_length=50)
    predicted_fashion_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.predicted_fashion_type}"
