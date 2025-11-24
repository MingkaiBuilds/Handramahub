from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from .drama import Drama


class Review(models.Model):
    drama = models.ForeignKey(
        Drama,
        on_delete=models.CASCADE,
        related_name="reviews",
        db_index=True,
    )
    rating = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )
    title = models.CharField(max_length=255, blank=True)
    body = models.TextField(blank=True)
    reviewer_name = models.CharField(max_length=255, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

    def __str__(self) -> str:
        base = f"{self.rating}★ - {self.drama.title}"
        if self.reviewer_name:
            return f"{base} (by {self.reviewer_name})"
        return base
