from django import forms
from .models import BookingInquiry


class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingInquiry
        fields = ['name', 'phone', 'email', 'service', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your name'}),
            'phone': forms.TextInput(attrs={'placeholder': '+237 6XX XXX XXX'}),
            'email': forms.EmailInput(attrs={'placeholder': 'your@email.com (optional)'}),
            'service': forms.Select(choices=[
                ('', 'Select a service'),
                ('Press-On Nails', 'Press-On Nails'),
                ('Custom Nail Set', 'Custom Nail Set'),
                ('Nail Application', 'Nail Application'),
            ]),
            'message': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Tell Thelma what you have in mind...'}),
        }
