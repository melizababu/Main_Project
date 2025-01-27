
# admin.py
#from django import forms
from django.contrib import admin
from .models import BusDetails
admin.site.register(BusDetails)


"""
class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = ['question', 'answer']  # List the fields you want in the admin form

class FAQAdmin(admin.ModelAdmin):
    form = FAQForm
    list_display = ('question', 'answer')  # Display the question and answer in the admin panel
    search_fields = ('question',)  # Enable searching based on the question

# Register models for admin interface
admin.site.register(Student)  # Django model

# Register the FAQ model with the custom admin form
admin.site.register(FAQ)
"""
