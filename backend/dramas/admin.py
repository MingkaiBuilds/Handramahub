from django.contrib import admin

from .models import Drama, Actor, DramaActor, Review


class DramaActorInline(admin.TabularInline):
    model = DramaActor
    extra = 1
    autocomplete_fields = ["actor"]


class ReviewInline(admin.TabularInline):
    model = Review
    extra = 1


@admin.register(Drama)
class DramaAdmin(admin.ModelAdmin):
    list_display = ["title", "year", "created_at"]
    search_fields = ["title", "description"]
    list_filter = ["year", "created_at"]
    ordering = ["-created_at"]
    inlines = [DramaActorInline, ReviewInline]


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ["name", "gender", "birth_year", "created_at"]
    search_fields = ["name", "nationality"]
    list_filter = ["gender", "birth_year"]
    ordering = ["name"]
    inlines = [DramaActorInline]


@admin.register(DramaActor)
class DramaActorAdmin(admin.ModelAdmin):
    list_display = ["drama", "actor", "character_name", "billing_order"]
    search_fields = ["drama__title", "actor__name", "character_name"]
    list_filter = ["drama", "actor"]
    ordering = ["billing_order", "actor"]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["drama", "rating", "reviewer_name", "created_at"]
    search_fields = ["drama__title", "reviewer_name", "title", "body"]
    list_filter = ["rating", "created_at", "drama"]
    ordering = ["-created_at"]
