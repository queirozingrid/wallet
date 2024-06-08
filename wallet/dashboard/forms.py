from django import forms
from dashboard import models

class AddWalletForm(forms.ModelForm):
    
    class Meta:
        model = models.Wallet
        fields = '__all__'