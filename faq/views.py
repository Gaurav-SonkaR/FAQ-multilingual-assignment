from rest_framework import generics
from .models import FAQ
from .serializers import FAQSerializer
from rest_framework.response import Response
from django.core.cache import cache
from django.shortcuts import render

class FAQListView(generics.ListAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def list(self, request, *args, **kwargs):
        lang = request.query_params.get("lang", "en")
        cache_key = f'faqs_{lang}'
        cached_data = cache.get(cache_key)

        if cached_data:
            return Response(cached_data)

        response = super().list(request, *args, **kwargs)
        for faq in response.data:
            faq['question'] = FAQ.objects.get(id=faq['id']).get_translated_data(lang)['question']
            faq['answer'] = FAQ.objects.get(id=faq['id']).get_translated_data(lang)['answer']
        cache.set(cache_key, response.data, timeout=3600)  # Cache for 1 hour
        return response

def home(request):
    lang = request.GET.get('lang', 'en')
    faqs = FAQ.objects.all()
    for faq in faqs:
        translated_data = faq.get_translated_data(lang)
        faq.question = translated_data['question']
        faq.answer = translated_data['answer']
    return render(request, 'faq.html', {'faqs': faqs, 'selected_lang': lang})
