from django.contrib import admin
from .models import akexam
from django.contrib.auth.models import User

@admin.register(akexam)
class akexamAdmin(admin.ModelAdmin):
    search_fields = ['exam_name', 'assigned_users__email']
    
    date_hierarchy = 'exam_date'
    
    filter_horizontal = ['assigned_users']
    
    list_filter = ['is_public']
    
    list_display = ['exam_name', 'exam_date', 'is_public']
    list_editable = ['is_public']