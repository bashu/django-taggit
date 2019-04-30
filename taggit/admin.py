from __future__ import unicode_literals

from django.contrib import admin
from parler.admin import TranslatableAdmin

from taggit.models import Tag, TaggedItem


class TaggedItemInline(admin.StackedInline):
    model = TaggedItem


@admin.register(Tag)
class TagAdmin(TranslatableAdmin):
    inlines = [TaggedItemInline]
    list_display = ["name", "slug", "language_column"]
    ordering = ["translations__name", "slug"]
    search_fields = ["name"]

    def get_prepopulated_fields(self, request, obj=None):
        return {"slug": ("name",)}  # needed for translated fields
