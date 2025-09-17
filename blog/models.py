from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
"""
Stores a single blog post entry related to :model:`auth.User`.
"""


class Post(models.Model):
    """
    Represents a blog post entry.

    Fields:
        title (CharField): The title of the post.
        slug (SlugField): URL-friendly identifier for the post.
        author (ForeignKey): Reference to the User who wrote the post.
        featured_image (CloudinaryField): Main image for the post.
        content (TextField): The main body of the post.
        created_on (DateTimeField): Timestamp when the post was created.
        status (IntegerField): Draft or Published status.
        excerpt (TextField): Optional short summary of the post.
        updated_on (DateTimeField): Timestamp when the post was last updated.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
        )
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"The title of this post is {self.title}"


class Comment(models.Model):
    """
    Represents a comment made on a blog post.

    Fields:
        post (ForeignKey): The blog post this comment is related to.
        author (ForeignKey): The user who wrote the comment.
        body (TextField): The content of the comment.
        approved (BooleanField): Whether the comment is approved for display.
        created_on (DateTimeField): Timestamp when the comment was created.
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
