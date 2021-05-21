from django import forms
from .models import Purchase, Product

class PurchaseForm(forms.ModelForm):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), label='Producto', widget=forms.Select(attrs={'class': 'form-control'}))
    price = forms.DecimalField(label="Precio", required=True, widget=forms.NumberInput(attrs={'class':'form-control'}))
    quantity = forms.IntegerField(label="Cantidad", required=True, widget=forms.NumberInput(attrs={'class':'form-control'}))


    class Meta:
        model = Purchase
        fields = ['product', 'price', 'quantity']
