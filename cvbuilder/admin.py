from django.contrib import admin
from .models import CV

@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'phone', 'created_at')
    search_fields = ('full_name', 'email', 'phone')

