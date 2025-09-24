from django.contrib import admin
from .models import About, CollaborateRequest
from django_summernote.admin import SummernoteModelAdmin


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    list_display = ('title', 'last_updated')
    
    fieldsets = (
        ('Profile Information', {
            'fields': ('title', 'profile_image')
        }),
        ('About Content', {
            'fields': ('content',),
            'description': 'Write your biography and about information here'
        }),
    )
    
    def last_updated(self, obj):
        return obj.updated_on.strftime("%B %d, %Y at %I:%M %p")
    last_updated.short_description = "Last Updated"

# Note: admin.ModelAdmin is the standard way of registering
#       our model with the admin panel. We do it differently
#       above because we are supplying Summernote fields.
#       If you want to customise the admin panel view in your
#       own projects, then inherit from admin.ModelAdmin like
#       we do below.


@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'email', 'message_preview', 'read', 'submitted_date')
    list_filter = ('read',)
    search_fields = ('name', 'email', 'message')
    actions = ['mark_as_read', 'mark_as_unread']
    
    fieldsets = (
        ('Requester Information', {
            'fields': ('name', 'email')
        }),
        ('Collaboration Details', {
            'fields': ('message',),
        }),
        ('Status', {
            'fields': ('read',),
            'description': 'Mark as read once you have reviewed this request'
        }),
    )
    
    def message_preview(self, obj):
        return obj.message[:75] + "..." if len(obj.message) > 75 else obj.message
    message_preview.short_description = "Message Preview"
    
    def submitted_date(self, obj):
        # Since there's no created date, we'll use the ID as a proxy
        return f"Request #{obj.id}"
    submitted_date.short_description = "Request ID"
    
    def mark_as_read(self, request, queryset):
        updated = queryset.update(read=True)
        self.message_user(request, f'{updated} requests were marked as read.')
    mark_as_read.short_description = "Mark selected requests as read"
    
    def mark_as_unread(self, request, queryset):
        updated = queryset.update(read=False)
        self.message_user(request, f'{updated} requests were marked as unread.')
    mark_as_unread.short_description = "Mark selected requests as unread"
