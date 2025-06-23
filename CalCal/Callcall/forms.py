from django import forms
from .modells import Topic, Entry

class topicform(forms.ModelForm):
    class meta:
        model = Topic
        fields = ['text']
        label = {'text': 'nome da label'}


class EntryForm(forms,ModelForm):
    class Meta:
        model = Entry
        filds = ['text']
        labels = {'text' : ''}
        widgets = {'text': forms.textarea(attrs={'cols':80})}