from rest_framework import serializers

from dramas.models import Drama, Actor, DramaActor, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = [
            "id",
            "drama",
            "rating",
            "title",
            "body",
            "reviewer_name",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class DramaSerializer(serializers.ModelSerializer):
    average_rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Drama
        fields = [
            "id",
            "title",
            "year",
            "description",
            "created_at",
            "updated_at",
            "average_rating",
        ]
        read_only_fields = ["id", "created_at", "updated_at", "average_rating"]


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = [
            "id",
            "name",
            "gender",
            "birth_year",
            "nationality",
            "bio",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class DramaActorSerializer(serializers.ModelSerializer):
    drama_title = serializers.CharField(source="drama.title", read_only=True)
    actor_name = serializers.CharField(source="actor.name", read_only=True)

    class Meta:
        model = DramaActor
        fields = [
            "id",
            "drama",
            "actor",
            "drama_title",
            "actor_name",
            "character_name",
            "billing_order",
            "notes",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]
