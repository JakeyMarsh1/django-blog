# Quick Reference: Django Label Editing

## Model Field Labels (verbose_name)

```python
# In your models.py
field_name = models.CharField(max_length=100, verbose_name="Display Name")
```

## Form Field Labels

```python
# Method 1: In Meta class
class MyForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['field1', 'field2']
        labels = {
            'field1': 'Custom Label 1',
            'field2': 'Custom Label 2'
        }

# Method 2: Override individual fields
class MyForm(forms.ModelForm):
    field1 = forms.CharField(label="Custom Label")
    
    class Meta:
        model = MyModel
        fields = ['field1']
```

## Admin Interface Labels

```python
# In your admin.py
class MyModelAdmin(admin.ModelAdmin):
    # Organize fields with labels
    fieldsets = (
        ('Section Name', {
            'fields': ('field1', 'field2'),
            'description': 'Optional description'
        }),
    )
    
    # Custom display methods
    def custom_display(self, obj):
        return obj.field_name
    custom_display.short_description = "Column Header Label"
    
    list_display = ('field1', 'custom_display')
```

## Template Labels

```html
<!-- Add descriptive text in templates -->
<label>Descriptive Label:</label> {{ object.field_name }}

<!-- Or use CSS classes for styling -->
<span class="field-label">Label:</span> 
<span class="field-value">{{ object.field_name }}</span>
```

## Common Use Cases

1. **User-friendly field names** in forms and admin
2. **Professional admin interface** with organized sections
3. **Better accessibility** with proper labels
4. **Consistent terminology** across your application
5. **Internationalization support** for multi-language sites

## Remember

- Model `verbose_name` affects admin and some form displays
- Form `labels` override model `verbose_name` in forms
- Admin custom methods need `short_description` for column headers
- Template labels are purely presentational and highly customizable