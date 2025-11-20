from django.db import models
from .drama import Drama
from .actor import Actor

class DramaActor(models.Model):
    drama = models.ForeignKey(
        Drama,
        on_delete=models.CASCADE,
        related_name="drama_actors"
    )
    actor = models.ForeignKey(
        Actor,
        on_delete=models.CASCADE,
        related_name="actor_dramas"
    )

    character_name = models.CharField(max_length=255, null=True, blank=True)
    billing_order = models.PositiveIntegerField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("drama", "actor")
        ordering = ["billing_order", "actor"]
        verbose_name = "Drama Actor Relationship"
        verbose_name_plural = "Drama Actor Relationships"

    def __str__(self):
        return f"{self.actor.name} in {self.drama.title}"
    