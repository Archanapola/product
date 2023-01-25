from django import forms
from .models import productMainModel


class productForm(forms.Form):
          Title=forms.CharField(label='Enter Studnt Name',max_length=30)
          Description=forms.CharField(label='Enter Studnt Name',max_length=80)
          price=forms.DecimalField(label='Enter Studnt Name',max_digits=10)
          unique_code=forms.UUIDField(label='Enter Studnt Name',primary_key=True)
          size=forms.IntegerField(label='Enter Studnt Name',max_length=30)
          quality=forms.CharField(label='Enter Studnt Name',max_length=30)
