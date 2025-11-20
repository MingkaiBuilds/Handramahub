from django.db import models

class Drama(models.Model):
    title = models.CharField(max_length=255, unique=True)
    year = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Drama"
        verbose_name_plural = "Dramas"

    def __str__(self):
        if self.year:
            return f"{self.title} ({self.year})"
        return self.title


