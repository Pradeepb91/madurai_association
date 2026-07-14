from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),

    path('reports/', views.reports, name='reports'),

    path('gallery/', views.gallery, name='gallery'),

    path('members/', views.members, name='members'),

    path('complaint/', views.complaint_create, name='complaint'),

    path('suggestion/', views.suggestion, name='suggestion'),

    path('suggestion-success/', views.suggestion_success, name='suggestion_success'),
	
    path('contact/', views.contact, name='contact'),

    path(
	"export-complaints/",
	views.export_complaints_excel,
	name="export_complaints"
),
   path(
    "export-suggestions/",
    views.export_suggestions_excel,
    name="export_suggestions"
),

path(
    "admin-dashboard/",
    views.admin_dashboard,
    name="admin_dashboard"
),

path(
    "admin-dashboard/",
    views.admin_dashboard,
    name="admin_dashboard",
),

]