from django.db import models

class GenderChoices(models.TextChoices):
    MALE = "M", "Male"
    FEMALE = "F", "Female"

class Actor(models.Model):
    name = models.CharField(max_length=255, unique=True)
    gender = models.CharField(
        max_length=1,
        choices=GenderChoices.choices,
        null=True,
        blank=True,
    )
    birth_year = models.IntegerField(null=True, blank=True)
    nationality = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Actor"
        verbose_name_plural = "Actors"
    
    def __str__(self):
        return self.name