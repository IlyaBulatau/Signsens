from django.contrib import admin

from main.models import Word

class WordAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'create_time')
    list_display_links = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Word, WordAdmin)
