from django.contrib import admin
from .models import Contact

# Register your models here.
# admin.site.register(Contact)
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'number', 'content']
    search_fields = ['name', 'email', 'number', 'content']
    # list_filter = ['name', 'email', 'number', 'content']
    list_per_page = 5
    # list_editable = ['email', 'number', 'content']
