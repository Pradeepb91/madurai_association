from django.db import models
from datetime import datetime


class Report(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField(blank=True)

    report_file = models.FileField(
        upload_to="reports/"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title



class GalleryEvent(models.Model):

    event_name = models.CharField(max_length=200)

    event_date = models.DateField()

    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event_name


class GalleryImage(models.Model):

    event = models.ForeignKey(
        GalleryEvent,
        on_delete=models.CASCADE,
        related_name="images"
    )

    image = models.ImageField(
        upload_to="gallery/"
    )

    def __str__(self):
        return self.event.event_name

class Member(models.Model):

    name = models.CharField(max_length=150)

    designation = models.CharField(max_length=150)

    photo = models.ImageField(
        upload_to="members/"
    )

    display_order = models.PositiveIntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["display_order"]




class Complaint(models.Model):
    CATEGORY_CHOICES = [
        ('Water Supply', 'Water Supply'),
        ('Drainage', 'Drainage'),
        ('Street Light', 'Street Light'),
        ('Road', 'Road'),
        ('Garbage', 'Garbage'),
        ('Security', 'Security'),
        ('Common Area', 'Common Area'),
        ('Others', 'Others'),
    ]

    house_number = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(max_length=10)

    complaint_category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES
    )

    complaint_description = models.TextField()

    complaint_date = models.DateTimeField(
        auto_now_add=True
    )

    photo = models.ImageField(
        upload_to='complaints/',
        blank=True,
        null=True
    )
	
    status = models.CharField(
    max_length=20,
    choices=[
        ("Pending", "Pending"),
        ("In Progress", "In Progress"),
        ("Resolved", "Resolved"),
        ("Rejected", "Rejected"),
    ],
    default="Pending",
)

    complaint_number = models.CharField(
    max_length=25,
    unique=True,
    blank=True,
    null=True
   )

    def save(self, *args, **kwargs):

        if not self.complaint_number:

            year = datetime.now().year

            last_complaint = Complaint.objects.order_by('-id').first()

            if last_complaint and last_complaint.complaint_number:

                try:
                    last_number = int(
                        last_complaint.complaint_number.split('-')[-1]
                    )

                except (ValueError, IndexError):
                    last_number = 0

            else:
                last_number = 0

            new_number = last_number + 1

            self.complaint_number = (
                f"MNL-CP-{year}-{new_number:04d}"
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.complaint_number} - {self.name}"
class Suggestion(models.Model):

    name = models.CharField(max_length=100)

    mobile = models.CharField(max_length=15)

    email = models.EmailField(blank=True, null=True)

    house_no = models.CharField(max_length=50)

    subject = models.CharField(max_length=200)

    suggestion = models.TextField()

    attachment = models.FileField(
        upload_to='suggestions/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    suggestion_number = models.CharField(
        max_length=25,
        unique=True,
        blank=True,
        null=True
    )

    def save(self, *args, **kwargs):

        if not self.suggestion_number:

            year = datetime.now().year

            last_suggestion = Suggestion.objects.order_by('-id').first()

            if last_suggestion and last_suggestion.suggestion_number:

                try:

                    last_number = int(
                        last_suggestion.suggestion_number.split('-')[-1]
                    )

                except (ValueError, IndexError):

                    last_number = 0

            else:

                last_number = 0

            new_number = last_number + 1

            self.suggestion_number = (
                f"MNL-SG-{year}-{new_number:04d}"
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.suggestion_number} - {self.subject}"

class AdminPortal(models.Model):

    class Meta:
        verbose_name = "🚀 Admin Portal"
        verbose_name_plural = "🚀 Admin Portal"

    def __str__(self):
        return "Open Association Portal"