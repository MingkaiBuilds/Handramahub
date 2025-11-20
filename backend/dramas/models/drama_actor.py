from django.db import models
from .drama import Drama
from .actor import Actor

class DramaActor(models.Model):
    drama = models.ForeignKey(
        Drama,
        on_delete=models.CASCADE,
        related_name="drama_actors",
        db_index=True
    )
    actor = models.ForeignKey(
        Actor,
        on_delete=models.CASCADE,
        related_name="actor_dramas",
        db_index=True
    )

    character_name = models.CharField(max_length=255, null=True, blank=True)
    billing_order = models.PositiveIntegerField(null=True, blank=True, db_index=True)
    notes = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["drama", "actor"],
                name="unique_drama_actor"
            )
        ]
        ordering = ["billing_order", "actor__name"]
        verbose_name = "Drama Actor Relationship"
        verbose_name_plural = "Drama Actor Relationships"

    def __str__(self):
        return f"{self.actor.name} in {self.drama.title}"
    