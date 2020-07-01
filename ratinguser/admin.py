from django.contrib import admin

from .models import RatingUser

class RatingUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'activation_key', 'ip')
    list_filter = ('email', 'ip')
    search_fields = ('email',)
admin.site.register(RatingUser, RatingUserAdmin)