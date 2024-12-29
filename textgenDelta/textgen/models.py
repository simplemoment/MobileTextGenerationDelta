from django.db import models


class TextGenerationSettings(models.Model):
    role_choices = [
        ('user', 'User'),
        ('assistant', 'Assistant'),
        ('system', 'System'),
    ]

    role = models.CharField(max_length=20, choices=role_choices, default='user')
    temperature = models.FloatField(default=0.7)
    max_tokens = models.IntegerField(default=2048)
    top_p = models.FloatField(default=1.0)
    top_k = models.IntegerField(default=50)

    def __str__(self):
        return f"{self.role} - Temp: {self.temperature}, Max Tokens: {self.max_tokens}"

