from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from association.models import (
    Complaint,
    Suggestion,
    Report,
    GalleryEvent,
    Member,
)


def _staff_only(request):
    if not request.user.is_staff:
        return redirect("admin_login")
    return None


@login_required(login_url="/accounts/login/")
def dashboard(request):
    block = _staff_only(request)
    if block:
        return block

    from_date = request.GET.get("from_date")
    to_date = request.GET.get("to_date")

    complaints = Complaint.objects.all()
    suggestions = Suggestion.objects.all()

    if from_date and to_date:
        complaints = complaints.filter(complaint_date__date__range=[from_date, to_date])
        suggestions = suggestions.filter(created_at__date__range=[from_date, to_date])

    return render(request, "portal/dashboard.html", {
        "total_complaints": Complaint.objects.count(),
        "total_suggestions": Suggestion.objects.count(),
        "filtered_complaints": complaints.count(),
        "filtered_suggestions": suggestions.count(),
        "from_date": from_date,
        "to_date": to_date,
    })


@login_required(login_url="/accounts/login/")
def complaint_management(request):
    block = _staff_only(request)
    if block:
        return block

    search = request.GET.get("search")
    complaints = Complaint.objects.all().order_by("-complaint_date")

    if search:
        complaints = complaints.filter(
            Q(complaint_number__icontains=search) |
            Q(house_number__icontains=search) |
            Q(mobile_number__icontains=search)
        )

    return render(request, "portal/complaints.html", {
        "complaints": complaints,
        "search": search,
    })


@login_required(login_url="/accounts/login/")
def complaint_detail(request, pk):
    block = _staff_only(request)
    if block:
        return block

    complaint = get_object_or_404(Complaint, pk=pk)

    if request.method == "POST":
        complaint.status = request.POST.get("status")
        complaint.save()
        print("STATUS =", request.POST.get("status"))
        return redirect("portal_complaint_detail", pk=complaint.pk)

    return render(
        request,
        "portal/complaint_detail.html",
        {
            "complaint": complaint,
        },
    )

@login_required(login_url="/accounts/login/")
def suggestion_management(request):
    block = _staff_only(request)
    if block:
        return block

    search = request.GET.get("search")
    suggestions = Suggestion.objects.all().order_by("-created_at")

    if search:
        suggestions = suggestions.filter(
            Q(name__icontains=search) |
            Q(mobile__icontains=search) |
            Q(house_no__icontains=search)
        )

    return render(request, "portal/suggestions.html", {
        "suggestions": suggestions,
        "search": search,
    })


@login_required(login_url="/accounts/login/")
def suggestion_detail(request, pk):
    block = _staff_only(request)
    if block:
        return block

    suggestion = get_object_or_404(Suggestion, pk=pk)

    return render(request, "portal/suggestion_detail.html", {
        "suggestion": suggestion,
    })


@login_required(login_url="/accounts/login/")
def report_management(request):
    block = _staff_only(request)
    if block:
        return block

    reports = Report.objects.all().order_by("-created_at")

    return render(request, "portal/reports.html", {
        "reports": reports,
    })


@login_required(login_url="/accounts/login/")
def gallery_management(request):
    block = _staff_only(request)
    if block:
        return block

    events = GalleryEvent.objects.all().order_by("-event_date")

    return render(request, "portal/gallery.html", {
        "events": events,
    })


@login_required(login_url="/accounts/login/")
def members_management(request):
    block = _staff_only(request)
    if block:
        return block

    members = Member.objects.all().order_by("display_order")

    return render(request, "portal/members.html", {
        "members": members,
    })
