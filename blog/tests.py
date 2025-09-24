from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment
from .forms import CommentForm

# Create your tests here.

class ModelLabelTests(TestCase):
    """Test that model verbose_name labels are working correctly."""
    
    def setUp(self):
        """Set up test data."""
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.post = Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=self.user,
            content='Test content',
            status=1
        )
    
    def test_post_field_labels(self):
        """Test Post model field labels."""
        post = Post.objects.get(id=self.post.id)
        
        # Test verbose_name labels
        title_label = post._meta.get_field('title').verbose_name
        content_label = post._meta.get_field('content').verbose_name
        author_label = post._meta.get_field('author').verbose_name
        created_on_label = post._meta.get_field('created_on').verbose_name
        status_label = post._meta.get_field('status').verbose_name
        
        self.assertEqual(title_label, 'Post Title')
        self.assertEqual(content_label, 'Post Content')
        self.assertEqual(author_label, 'Author')
        self.assertEqual(created_on_label, 'Date Created')
        self.assertEqual(status_label, 'Publication Status')
    
    def test_comment_field_labels(self):
        """Test Comment model field labels."""
        comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            body='Test comment',
            approved=True
        )
        
        # Test verbose_name labels
        post_label = comment._meta.get_field('post').verbose_name
        author_label = comment._meta.get_field('author').verbose_name
        body_label = comment._meta.get_field('body').verbose_name
        approved_label = comment._meta.get_field('approved').verbose_name
        created_on_label = comment._meta.get_field('created_on').verbose_name
        
        self.assertEqual(post_label, 'Blog Post')
        self.assertEqual(author_label, 'Comment Author')
        self.assertEqual(body_label, 'Comment Text')
        self.assertEqual(approved_label, 'Approved for Display')
        self.assertEqual(created_on_label, 'Date Posted')
    
    def test_comment_form_labels(self):
        """Test CommentForm custom labels."""
        form = CommentForm()
        
        # Test that form has custom label
        self.assertEqual(form.fields['body'].label, 'Your Comment')
        
        # Test that form has placeholder
        self.assertEqual(
            form.fields['body'].widget.attrs['placeholder'], 
            'Write your comment here...'
        )
