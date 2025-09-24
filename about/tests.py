from django.test import TestCase
from .models import About, CollaborateRequest
from .forms import CollaborateForm

# Create your tests here.

class AboutModelLabelTests(TestCase):
    """Test that About model verbose_name labels are working correctly."""
    
    def test_about_field_labels(self):
        """Test About model field labels."""
        about = About.objects.create(
            title='Test About',
            content='Test content'
        )
        
        # Test verbose_name labels
        title_label = about._meta.get_field('title').verbose_name
        profile_image_label = about._meta.get_field('profile_image').verbose_name
        updated_on_label = about._meta.get_field('updated_on').verbose_name
        content_label = about._meta.get_field('content').verbose_name
        
        self.assertEqual(title_label, 'Profile Title')
        self.assertEqual(profile_image_label, 'Profile Photo')
        self.assertEqual(updated_on_label, 'Last Updated')
        self.assertEqual(content_label, 'About Content')
    
    def test_collaborate_request_field_labels(self):
        """Test CollaborateRequest model field labels."""
        request = CollaborateRequest.objects.create(
            name='Test User',
            email='test@example.com',
            message='Test collaboration message'
        )
        
        # Test verbose_name labels
        name_label = request._meta.get_field('name').verbose_name
        email_label = request._meta.get_field('email').verbose_name
        message_label = request._meta.get_field('message').verbose_name
        read_label = request._meta.get_field('read').verbose_name
        
        self.assertEqual(name_label, 'Full Name')
        self.assertEqual(email_label, 'Email Address')
        self.assertEqual(message_label, 'Collaboration Message')
        self.assertEqual(read_label, 'Mark as Read')
    
    def test_collaborate_form_labels(self):
        """Test CollaborateForm custom labels."""
        form = CollaborateForm()
        
        # Test that form has custom labels
        self.assertEqual(form.fields['name'].label, 'Your Name')
        self.assertEqual(form.fields['email'].label, 'Your Email Address')
        self.assertEqual(form.fields['message'].label, 'Tell us about your collaboration idea')
        
        # Test that form has placeholders
        self.assertEqual(
            form.fields['name'].widget.attrs['placeholder'], 
            'Enter your full name'
        )
        self.assertEqual(
            form.fields['email'].widget.attrs['placeholder'], 
            'your.email@example.com'
        )
