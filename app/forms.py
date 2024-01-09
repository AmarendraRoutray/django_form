from django import forms
from .models import *


class TopicForm(forms.Form):
    TopicName=forms.CharField()
    


class WebpageForm(forms.Form):
    # TopicName = forms.ModelChoiceField(queryset=Topic.objects.all())
    
    tl=[[to.topic_name,to.topic_name] for to in Topic.objects.all()]
    TopicName = forms.ChoiceField(choices=tl)
    
    Name = forms.CharField()
    Email = forms.EmailField()
    Url = forms.URLField()
    


class AccessRecordForm(forms.Form):
    
    wl = [[wo.pk,wo.name] for wo in Webpage.objects.all()]
    Name = forms.ChoiceField(choices=wl)
    
    # Name = forms.ModelChoiceField(queryset=Webpage.objects.all())
    # Name = forms.ModelChoiceField(queryset=Webpage.objects.all(),widget=forms.RadioSelect)
    # Name = forms.ModelMultipleChoiceField(queryset=Webpage.objects.all(),widget=forms.CheckboxSelectMultiple)
    
    Author = forms.CharField()
    Date = forms.DateField()
    