
from django import forms

class InquiryForm(forms.Form):
    name = forms.CharField(label='Name', max_length=30)
    email = forms.EmailField(label='Email address')
    title = forms.CharField(label='Title', max_length=30)
    message = forms.CharField(label='Message', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control col9'
        self.fields['name'].widget.attrs['placeholder'] = 'Enter your name'

        self.fields['email'].widget.attrs['class'] = 'form-control col11'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your Email address'

        self.fields['title'].widget.attrs['class'] = 'form-control col11'
        self.fields['title'].widget.attrs['placeholder'] = 'Enter the title'

        self.fields['message'].widget.attrs['class'] = 'form-control col12'
        self.fields['message'].widget.attrs['placeholder'] = 'Enter a message'
