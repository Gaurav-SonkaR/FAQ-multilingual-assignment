from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    translated_question = serializers.SerializerMethodField()
    translated_answer = serializers.SerializerMethodField()

    class Meta:
        model = FAQ
        fields = ['id', 'question', 'translated_question', 'translated_answer', 'answer', 'language']

    def get_translated_question(self, obj):
        request = self.context.get('request', None)
        lang = request.query_params.get('lang', 'en')
        return obj.get_translated_data(lang)['question']

    def get_translated_answer(self, obj):
        request = self.context.get('request', None)
        lang = request.query_params.get('lang', 'en')
        return obj.get_translated_data(lang)['answer']
