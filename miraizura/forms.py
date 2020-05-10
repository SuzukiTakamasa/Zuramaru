
from django import forms
from django.core.mail import EmailMessage
from .models import Diary

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
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email address'

        self.fields['title'].widget.attrs['class'] = 'form-control col11'
        self.fields['title'].widget.attrs['placeholder'] = 'Enter the title'

        self.fields['message'].widget.attrs['class'] = 'form-control col12'
        self.fields['message'].widget.attrs['placeholder'] = 'Enter a message'

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        title = self.cleaned_data['title']
        message = self.cleaned_data['message']

        subject = "Inquiry {}".format(title)
        message = "Sender's name: {0}\nEmail address: {1}\nMessage:\n{2}".format(name, email, message)
        from_email = 'admin@example.com'
        to_list = ['test@example.com']
        cc_list = [email]

        message = EmailMessage(subject=subject, body=message, from_email=from_email, to=to_list, cc=cc_list)
        message.send()

class DiaryCreateForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ('title', 'content',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'