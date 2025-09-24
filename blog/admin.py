from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    
    list_display = ('title', 'author', 'publication_status', 'date_created')
    search_fields = ['title', 'content', 'author__username']
    list_filter = ('status', 'created_on', 'author')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'author')
        }),
        ('Content', {
            'fields': ('content', 'excerpt', 'featured_image')
        }),
        ('Publication', {
            'fields': ('status',),
            'description': 'Control whether this post is published or remains as a draft'
        }),
    )
    
    def publication_status(self, obj):
        return "Published" if obj.status == 1 else "Draft"
    publication_status.short_description = "Status"
    
    def date_created(self, obj):
        return obj.created_on.strftime("%B %d, %Y")
    date_created.short_description = "Created On"


# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'comment_preview', 'approved', 'date_posted')
    list_filter = ('approved', 'created_on', 'post')
    search_fields = ['author__username', 'body', 'post__title']
    actions = ['approve_comments']
    
    fieldsets = (
        ('Comment Details', {
            'fields': ('post', 'author', 'body')
        }),
        ('Moderation', {
            'fields': ('approved',),
            'description': 'Mark as approved to show this comment on the website'
        }),
    )
    
    def comment_preview(self, obj):
        return obj.body[:50] + "..." if len(obj.body) > 50 else obj.body
    comment_preview.short_description = "Comment Preview"
    
    def date_posted(self, obj):
        return obj.created_on.strftime("%B %d, %Y")
    date_posted.short_description = "Posted On"
    
    def approve_comments(self, request, queryset):
        updated = queryset.update(approved=True)
        self.message_user(request, f'{updated} comments were approved.')
    approve_comments.short_description = "Mark selected comments as approved"


admin.site.register(Comment)
