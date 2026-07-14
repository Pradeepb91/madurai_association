from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from openpyxl import Workbook

from .models import Report, GalleryEvent, Member, Complaint, Suggestion
from .forms import ComplaintForm, SuggestionForm


from django.http import HttpResponse

def home(request):
    return HttpResponse("Madurai Association Website is Live")


def reports(request):
    reports = Report.objects.all().order_by("-created_at")
    return render(request, "reports.html", {"reports": reports})


def gallery(request):
    events = GalleryEvent.objects.all().order_by("-event_date")
    return render(request, "gallery.html", {"events": events})


def members(request):
    members = Member.objects.all().order_by("display_order")
    return render(request, "members.html", {"members": members})


def complaint_create(request):
    if request.method == "POST":
        form = ComplaintForm(request.POST, request.FILES)
        if form.is_valid():
            complaint = form.save()
            return render(request, "complaint_success.html", {"complaint": complaint})
    else:
        form = ComplaintForm()
    return render(request, "complaint_form.html", {"form": form})


def suggestion(request):
    if request.method == "POST":
        form = SuggestionForm(request.POST, request.FILES)
        if form.is_valid():
            suggestion = form.save()
            return render(request, "association/suggestion_success.html", {"suggestion": suggestion})
    else:
        form = SuggestionForm()
    return render(request, "association/suggestion.html", {"form": form})


def suggestion_success(request):
    return render(request, "association/suggestion_success.html")


def contact(request):
    return render(request, "contact.html")


def export_complaints_excel(request):
    from_date = request.GET.get("from_date")
    to_date = request.GET.get("to_date")
    qs = Complaint.objects.all().order_by("-complaint_date")
    if from_date and to_date:
        qs = qs.filter(complaint_date__date__range=[from_date, to_date])

    wb = Workbook()
    ws = wb.active
    ws.title = "Complaints"
    ws.append(["Complaint Number","Date","House Number","Name","Mobile","Category","Complaint"])

    for c in qs:
        ws.append([
            c.complaint_number,
            c.complaint_date.strftime("%d-%m-%Y %H:%M"),
            c.house_number,
            c.name,
            c.mobile_number,
            c.complaint_category,
            c.complaint_description
        ])

    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response["Content-Disposition"] = 'attachment; filename="Complaints.xlsx"'
    wb.save(response)
    return response


def export_suggestions_excel(request):
    from_date = request.GET.get("from_date")
    to_date = request.GET.get("to_date")
    qs = Suggestion.objects.all().order_by("-created_at")
    if from_date and to_date:
        qs = qs.filter(created_at__date__range=[from_date, to_date])

    wb = Workbook()
    ws = wb.active
    ws.title = "Suggestions"
    ws.append(["Suggestion Number","Date","House Number","Name","Mobile","Subject","Suggestion"])

    for s in qs:
        ws.append([
            s.suggestion_number,
            s.created_at.strftime("%d-%m-%Y %H:%M"),
            s.house_no,
            s.name,
            s.mobile,
            s.subject,
            s.suggestion
        ])

    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response["Content-Disposition"] = 'attachment; filename="Suggestions.xlsx"'
    wb.save(response)
    return response


@login_required(login_url="/admin/login/")
def admin_dashboard(request):
    return render(request, "admin_dashboard.html", {
        "total_complaints": Complaint.objects.count(),
        "total_suggestions": Suggestion.objects.count(),
    })
    