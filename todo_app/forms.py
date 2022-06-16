from django import forms
from django.db.models import fields
from.models import TodoList


class Todoform(forms.ModelForm):
    
    class Meta:
        
        model = TodoList
        fields = '__all__'
