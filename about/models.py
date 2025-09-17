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
    title = models.CharField(max_length=200)
    profile_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

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
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"
