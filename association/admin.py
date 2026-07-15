from django.contrib import admin
from django.utils.html import format_html
from .models import Report, GalleryEvent, GalleryImage, Member, Complaint, Suggestion

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display=("title","created_at")
    search_fields=("title",)

class GalleryImageInline(admin.TabularInline):
    model=GalleryImage
    extra=1

@admin.register(GalleryEvent)
class GalleryEventAdmin(admin.ModelAdmin):
    list_display=("event_name","event_date")
    search_fields=("event_name",)
    inlines=[GalleryImageInline]

@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display=("event","image_preview","caption")
    search_fields=("event__event_name","caption")
    def image_preview(self,obj):
        image=obj.get_image()
        if image:
            return format_html('<img src="{}" width="120" style="border-radius:8px;">',image)
        return "-"
    image_preview.short_description="Preview"

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display=("photo_preview","name","designation","display_order","is_active")
    list_filter=("is_active",)
    search_fields=("name","designation")
    ordering=("display_order",)
    def photo_preview(self,obj):
        photo=obj.get_photo()
        if photo:
            return format_html('<img src="{}" width="70" height="70" style="border-radius:50%;object-fit:cover;">',photo)
        return "-"
    photo_preview.short_description="Photo"

@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display=("complaint_number","house_number","name","mobile_number","complaint_category","status","complaint_date")
    list_filter=("status","complaint_category")
    search_fields=("complaint_number","name","house_number","mobile_number")
    ordering=("-complaint_date",)

@admin.register(Suggestion)
class SuggestionAdmin(admin.ModelAdmin):
    list_display=("suggestion_number","house_no","name","mobile","subject","created_at")
    search_fields=("suggestion_number","house_no","name","mobile","subject")
    ordering=("-created_at",)
