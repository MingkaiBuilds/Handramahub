from django.urls import path

from .views import (
    DramaListCreateView,
    DramaDetailView,
    ActorListCreateView,
    ActorDetailView,
    DramaActorListCreateView,
    DramaActorDetailView,
    DramaCastListView,
    ReviewListCreateView,
    ReviewDetailView,
    DramaReviewListCreateView,
)


urlpatterns = [
    # Dramas
    path("dramas/", DramaListCreateView.as_view(), name="dramas-list"),
    path("dramas/<int:pk>/", DramaDetailView.as_view(), name="dramas-detail"),
    path(
        "dramas/<int:drama_id>/cast/",
        DramaCastListView.as_view(),
        name="dramas-cast",
    ),
    path(
        "dramas/<int:drama_id>/reviews/",
        DramaReviewListCreateView.as_view(),
        name="dramas-reviews",
    ),

    # Actors
    path("actors/", ActorListCreateView.as_view(), name="actors-list"),
    path("actors/<int:pk>/", ActorDetailView.as_view(), name="actors-detail"),

    # DramaActor
    path(
        "drama-actors/",
        DramaActorListCreateView.as_view(),
        name="drama-actors-list",
    ),
    path(
        "drama-actors/<int:pk>/",
        DramaActorDetailView.as_view(),
        name="drama-actors-detail",
    ),

    # Reviews
    path("reviews/", ReviewListCreateView.as_view(), name="reviews-list"),
    path("reviews/<int:pk>/", ReviewDetailView.as_view(), name="reviews-detail"),
]
