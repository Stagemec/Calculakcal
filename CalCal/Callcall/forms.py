from django import forms
from .modells import Topic

class topicform(forms.ModelForm):
    class meta:
        model = Topic
        fields = ['text']
        label = {'text': 'nome da label'}