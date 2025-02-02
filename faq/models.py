from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

class FAQ(models.Model):
    LANGUAGE_CHOICES = [
        ('en', 'English'),
        ('hi', 'Hindi'),
        ('bn', 'Bengali'),
    ]

    question = models.TextField()
    answer = RichTextField()
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, default='en')
    question_hi = models.TextField(blank=True, null=True)
    answer_hi = RichTextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)
    answer_bn = RichTextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        translator = Translator()
        if not self.question_hi or not self.answer_hi:
            self.question_hi = translator.translate(self.question, dest='hi').text
            self.answer_hi = translator.translate(self.answer, dest='hi').text
        if not self.question_bn or not self.answer_bn:
            self.question_bn = translator.translate(self.question, dest='bn').text
            self.answer_bn = translator.translate(self.answer, dest='bn').text
        super().save(*args, **kwargs)

    def get_translated_data(self, lang="en"):
        if lang == "hi":
            return {"question": self.question_hi, "answer": self.answer_hi}
        elif lang == "bn":
            return {"question": self.question_bn, "answer": self.answer_bn}
        return {"question": self.question, "answer": self.answer}
    
    def __str__(self):
        return self.question
