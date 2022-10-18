from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['email','username', 'slug', 'first_name', 'last_name', 'birth_date']
    list_display_links = ['email', 'slug']
    search_fields = ['lsat_name']
    list_filter = ['birth_date']
    fields = ['email', 'username', 'slug', 'first_name', 'last_name', 'birth_date', 'staff', 'admin', 'created_at']
    readonly_fields = ['email', 'username', 'slug', 'first_name', 'last_name', 'birth_date', 'created_at']