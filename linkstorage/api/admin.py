from django.contrib import admin
from .models import CustomUser, Link, Collection

class CustomUserAdmin(admin.ModelAdmin):
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active')
    list_filter = ('is_staff', 'is_active')
    fields = ('email','password',('is_staff', 'is_active'), 'date_joined')
    readonly_fields = ('date_joined',)
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Link)
admin.site.register(Collection)


