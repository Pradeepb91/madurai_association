from django.urls import path
from . import views

urlpatterns = [

    path(
        "",
        views.dashboard,
        name="portal_dashboard"
    ),

    path(
        "complaints/",
        views.complaint_management,
        name="portal_complaints"
    ),

    path(
        "complaints/<int:pk>/",
        views.complaint_detail,
        name="portal_complaint_detail"
    ),

    path(
        "suggestions/",
        views.suggestion_management,
        name="portal_suggestions"
    ),

    path(
        "suggestions/<int:pk>/",
        views.suggestion_detail,
        name="portal_suggestion_detail"
    ),

    path(
        "reports/",
        views.report_management,
        name="portal_reports"
    ),

    path(
        "gallery/",
        views.gallery_management,
        name="portal_gallery"
    ),

    path(
        "members/",
        views.members_management,
        name="portal_members"
    ),

]