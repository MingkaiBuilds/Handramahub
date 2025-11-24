from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from dramas.models import Drama, Actor, DramaActor
from .serializers import DramaSerializer, ActorSerializer, DramaActorSerializer

# Drama Views
class DramaListCreateView(generics.ListCreateAPIView):
    queryset = Drama.objects.all().order_by("-created_at")
    serializer_class = DramaSerializer

    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ["title", "year", "created_at"]
    filterset_fields = ["year"]

class DramaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drama.objects.all().prefetch_related("drama_actors_actor")
    serializer_class = DramaSerializer

# Actor Views
class ActorListCreateView(generics.ListCreateAPIView):
    queryset = Actor.objects.all().order_by("name")
    serializer_class = ActorSerializer

    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ["name", "birth_year", "gender"]
    filterset_fields = ["gender", "birth_year"]

class ActorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all().prefetch_related("actor_dramas_drama")
    serializer_class = ActorSerializer


# DramaActor Views
class DramaActorListCreateView(generics.ListCreateAPIView):
    queryset = DramaActor.objects.all().select_related("drama", "actor")
    serializer_class = DramaActorSerializer

    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ["billing_order", "actor__name"]
    filterset_fields = ["drama", "actor"]

class DramaActorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DramaActor.objects.all().select_related("drama", "actor")
    serializer_class = DramaActorSerializer

# Custom Views
class DramaCastListView(generics.ListAPIView):
    serializer_class = DramaActorSerializer

    def get_queryset(self):
        drama_id = self.kwargs["drama_id"]
        return DramaActor.objects.filter(drama_id=drama_id).select_related("actor", "drama").order_by("billing_order")