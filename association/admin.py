from django.contrib import admin
from .models import (
    Report,
    GalleryEvent,
    GalleryImage,
    Member,
)

admin.site.site_header = "Madurai New LIG Welfare Association"
admin.site.site_title = "Association Admin"
admin.site.index_title = "Administration"


@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ("title", "created_at")
    search_fields = ("title",)


class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 1


@admin.register(GalleryEvent)
class GalleryEventAdmin(admin.ModelAdmin):
    list_display = ("event_name", "event_date")
    inlines = [GalleryImageInline]


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ("name", "designation", "display_order")
    ordering = ("display_order",)