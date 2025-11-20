from django.contrib import admin
from .models import Drama, Actor, DramaActor

# Register your models here.
class DramaActorInline(admin.TabularInline):
    model = DramaActor
    extra = 1
    autocomplete_fields = ["actor"]

@admin.register(Drama)
class DramaAdmin(admin.ModelAdmin):
    list_display = ["title", "year"]
    search_fields = ["title", "description"]
    list_filter = ["year", "created_at"]
    ordering = ["-created_at"]
    inlines = [DramaActorInline]

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
    list_select_related = ["drama", "actor"]
    raw_id_fields = ["drama", "actor"]



