from django.contrib import admin
from .models import akexam

@admin.register(akexam)
class akexamAdmin(admin.ModelAdmin):
    list_display = ("exam_name", "exam_date", "is_public")
    list_filter = ("is_public", "exam_date")
    search_fields = ("exam_name",)