import pytest
from rest_framework.test import APIClient
from .models import FAQ

@pytest.mark.django_db
def test_faq_api():
    FAQ.objects.create(question="What is Django?", answer="Django is a web framework.", language="en")

    client = APIClient()
    response = client.get('/api/faqs/?lang=hi')
    
    assert response.status_code == 200
