from django import forms
from .models import *

class Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Form, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['roll_no'].widget.attrs['readonly'] = True
    
    class Meta:
        model = student
        fields = "__all__"
        widgets={
            'roll_no':forms.NumberInput(attrs={'class':'input input-bordered w-full max-w-xs'}),
            'name':forms.TextInput(attrs={'class':'input input-bordered w-full max-w-xs'}),
            'current_class':forms.TextInput(attrs={'class':'input input-bordered w-full max-w-xs'}),
            'age':forms.NumberInput(attrs={'class':'input input-bordered w-full max-w-xs'}),
        }
      
