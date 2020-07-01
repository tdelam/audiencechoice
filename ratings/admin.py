from django.contrib import admin
from models import Rating, RatingEvent


class RatingEventAdmin(admin.ModelAdmin):
    list_display = ('key', 'ip', 'email', 'value', 'delete_vote')
    search_fields = ('email',)
    list_filter = ('key', 'email')
admin.site.register(RatingEvent, RatingEventAdmin)

class RatingAdmin(admin.ModelAdmin):
    list_display = ('key', 'total_rating', 'total_votes')
admin.site.register(Rating, RatingAdmin)
