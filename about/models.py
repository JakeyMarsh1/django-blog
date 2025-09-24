from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class About(models.Model):
    """
    Represents the About section/profile for the site owner.

    Fields:
        title (CharField): The title or name of the profile.
        profile_image (CloudinaryField): Profile image for the about section.
        updated_on (DateTimeField): Timestamp when the profile was last updated.
        content (TextField): Main content or biography for the profile.
    """
    title = models.CharField(max_length=200, verbose_name="Profile Title")
    profile_image = CloudinaryField('image', default='placeholder', verbose_name="Profile Photo")
    updated_on = models.DateTimeField(auto_now=True, verbose_name="Last Updated")
    content = models.TextField(verbose_name="About Content")

    class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Pages"

    def __str__(self):
        return self.title


class CollaborateRequest(models.Model):
    """
    Represents a request to collaborate sent via the About page.

    Fields:
        name (CharField): Name of the person requesting collaboration.
        email (EmailField): Email address of the requester.
        message (TextField): The collaboration message or inquiry.
        read (BooleanField): Whether the request has been read/processed.
    """
    name = models.CharField(max_length=200, verbose_name="Full Name")
    email = models.EmailField(verbose_name="Email Address")
    message = models.TextField(verbose_name="Collaboration Message")
    read = models.BooleanField(default=False, verbose_name="Mark as Read")

    class Meta:
        verbose_name = "Collaboration Request"
        verbose_name_plural = "Collaboration Requests"

    def __str__(self):
        return f"Collaboration request from {self.name}"
