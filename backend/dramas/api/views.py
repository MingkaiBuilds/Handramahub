from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters

from dramas.models import Drama, Actor, DramaActor, Review
from .serializers import (
    DramaSerializer,
    ActorSerializer,
    DramaActorSerializer,
    ReviewSerializer,
)


# -----------------------------
# DRAMA VIEWS
# -----------------------------


class DramaListCreateView(generics.ListCreateAPIView):
    queryset = (
        Drama.objects
        .all()
        .annotate(average_rating=Avg("reviews__rating"))
        .order_by("-created_at")
    )
    serializer_class = DramaSerializer

    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ["title", "year", "created_at"]
    filterset_fields = ["year"]


class DramaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = (
        Drama.objects
        .all()
        .annotate(average_rating=Avg("reviews__rating"))
        .prefetch_related("drama_actors__actor", "reviews")
    )
    serializer_class = DramaSerializer


# -----------------------------
# ACTOR VIEWS
# -----------------------------


class ActorListCreateView(generics.ListCreateAPIView):
    queryset = Actor.objects.all().order_by("name")
    serializer_class = ActorSerializer

    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ["name", "birth_year", "gender"]
    filterset_fields = ["gender", "birth_year"]


class ActorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all().prefetch_related("actor_dramas__drama")
    serializer_class = ActorSerializer


# -----------------------------
# DRAMAACTOR VIEWS
# -----------------------------


class DramaActorListCreateView(generics.ListCreateAPIView):
    queryset = DramaActor.objects.select_related("drama", "actor").all()
    serializer_class = DramaActorSerializer

    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ["billing_order", "actor__name"]
    filterset_fields = ["drama", "actor"]


class DramaActorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = DramaActor.objects.select_related("drama", "actor").all()
    serializer_class = DramaActorSerializer


class DramaCastListView(generics.ListAPIView):
    serializer_class = DramaActorSerializer

    def get_queryset(self):
        drama_id = self.kwargs["drama_id"]
        return (
            DramaActor.objects
            .filter(drama_id=drama_id)
            .select_related("actor", "drama")
            .order_by("billing_order", "actor__name")
        )


# -----------------------------
# REVIEW VIEWS
# -----------------------------


class ReviewListCreateView(generics.ListCreateAPIView):
    """
    List all reviews or create a new review.
    Optional filters: ?drama=<id>&rating=5
    """

    queryset = Review.objects.select_related("drama").all()
    serializer_class = ReviewSerializer

    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = ["created_at", "rating"]
    filterset_fields = ["drama", "rating"]


class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.select_related("drama").all()
    serializer_class = ReviewSerializer


class DramaReviewListCreateView(generics.ListCreateAPIView):
    """
    List or create reviews for a specific drama: /api/dramas/<drama_id>/reviews/
    """

    serializer_class = ReviewSerializer

    def get_queryset(self):
        drama_id = self.kwargs["drama_id"]
        return (
            Review.objects
            .filter(drama_id=drama_id)
            .select_related("drama")
            .order_by("-created_at")
        )

    def perform_create(self, serializer):
        drama_id = self.kwargs["drama_id"]
        serializer.save(drama_id=drama_id)
