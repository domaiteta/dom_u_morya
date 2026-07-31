from django import forms

from orders.models import Order


class OrderForm(forms.ModelForm):
    personal_data = forms.BooleanField(label='Я согласен на обработку персональных данных')

    class Meta:
        model = Order
        fields = ['house', 'name', 'phone']
        widgets = {
            "house": forms.HiddenInput()
        }
