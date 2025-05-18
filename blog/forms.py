from django import forms

from blog.models import Contact


class ContactForm(forms.Form):
    name = forms.CharField(max_length=120, label='Name')
    email = forms.EmailField(label='Email')
    subject = forms.CharField(max_length=120, label='Subject')
    message = forms.CharField(widget=forms.Textarea, label='Message')

