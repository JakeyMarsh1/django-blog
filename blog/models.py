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
    title = models.CharField(max_length=200, unique=True, verbose_name="Post Title")
    slug = models.SlugField(max_length=200, unique=True, verbose_name="URL Slug")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts", verbose_name="Author"
        )
    featured_image = CloudinaryField('image', default='placeholder', verbose_name="Featured Image")
    content = models.TextField(verbose_name="Post Content")
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Date Created")
    status = models.IntegerField(choices=STATUS, default=0, verbose_name="Publication Status")
    excerpt = models.TextField(blank=True, verbose_name="Short Summary")
    updated_on = models.DateTimeField(auto_now=True, verbose_name="Last Updated")

    class Meta:
        ordering = ["-created_on"]
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"

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
        Post, on_delete=models.CASCADE, related_name="comments", verbose_name="Blog Post"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter", verbose_name="Comment Author"
    )
    body = models.TextField(verbose_name="Comment Text")
    approved = models.BooleanField(default=False, verbose_name="Approved for Display")
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Date Posted")

    class Meta:
        ordering = ["-created_on"]
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return f"Comment {self.body} by {self.author}"
