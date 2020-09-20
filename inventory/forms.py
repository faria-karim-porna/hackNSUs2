from django import forms
from inventory.models import Purchase

class PurchaseForm(forms.ModelForm):
    
    class Meta:
        model = Purchase
        fields = "__all__"
