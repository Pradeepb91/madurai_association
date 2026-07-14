from django.db import models
class Gallery(models.Model):

    event_name = models.CharField(max_length=200)

    event_date = models.DateField()

    description = models.TextField(blank=True)

    image1 = models.ImageField(upload_to="gallery/")

    image2 = models.ImageField(upload_to="gallery/", blank=True, null=True)

    image3 = models.ImageField(upload_to="gallery/", blank=True, null=True)

    image4 = models.ImageField(upload_to="gallery/", blank=True, null=True)

    image5 = models.ImageField(upload_to="gallery/", blank=True, null=True)

    image6 = models.ImageField(upload_to="gallery/", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.event_name