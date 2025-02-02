from django.contrib import admin
from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'language', 'get_translated_question')

    def get_translated_question(self, obj):
        return obj.get_translated_question()

    get_translated_question.short_description = "Translated Question"
