from django.contrib import admin
from .models import TextGenerationSettings

@admin.register(TextGenerationSettings)
class TextGenerationSettingsAdmin(admin.ModelAdmin):
    list_display = ('role', 'temperature', 'max_tokens', 'top_p', 'top_k')
    search_fields = ('role',)

