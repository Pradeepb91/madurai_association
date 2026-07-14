from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from association.models import Complaint, Suggestion


@login_required(login_url="/accounts/login/")
def dashboard(request):

    context = {
        "total_complaints": Complaint.objects.count(),
        "total_suggestions": Suggestion.objects.count(),
    }

    return render(
        request,
        "portal/dashboard.html",
        context,
    )