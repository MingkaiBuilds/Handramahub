from django.urls import path
from .views import (
    DramaListCreateView,
    DramaDetailView,
    ActorListCreateView,
    ActorDetailView,
    DramaActorListCreateView,
    DramaActorDetailView,
    DramaCastListView
)

urlpatterns = [
    # Drama endpoints
    path("dramas/", DramaListCreateView.as_view(), name="drama-list"),
    path("dramas/<int:pk>/", DramaDetailView.as_view(), name="drama-detail"),
    path("dramas/<int:drama_id>/cast/", DramaCastListView.as_view(), name="drama-cast"),

    # Actor endpoints
    path("actors/", ActorListCreateView.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetailView.as_view(), name="actor-detail"),

    # DramaActor endpoints
    path("drama-actors/", DramaActorListCreateView.as_view(), name="drama-actor-list"),
    path("drama-actors/<int:pk>/", DramaActorDetailView.as_view(), name="drama-actor-detail"),

]