from rest_framework import serializers
from dramas.models import Actor, Drama, DramaActor

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
        ]

class DramaActorSerializer(serializers.ModelSerializer):
    actor = ActorSerializer(read_only=True)

    class Meta:
        model = DramaActor
        fields = [
            "id",
            "actor",
            "character_name",
            "billing_order",
        ]

class DramaSerializer(serializers.ModelSerializer):
    cast = serializers.SerializerMethodField()

    class Meta:
        model = Drama
        fields = [
            "id",
            "title",
            "year",
            "description",
            "cast",
        ]
    
    def get_cast(self, obj):
        qs = obj.drama_actors.all()
        return DramaActorSerializer(qs, many=True).data
