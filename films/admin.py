from django.contrib import admin

from .models import Film, Category


class FilmAdmin(admin.ModelAdmin):
    list_display = ('title','active')
    list_editable = ('active',)
    search_fields = ('title',)
admin.site.register(Film, FilmAdmin)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(Category, CategoryAdmin)
