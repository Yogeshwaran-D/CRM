from django import forms
from .models import Leads

class LeadModelForm(forms.ModelForm):
    class Meta :
        model=Leads
        fields=(
            "first_name" ,
            "last_name" ,
            "age" ,
            "agent" ,
        )
