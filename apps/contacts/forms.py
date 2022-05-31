from django import forms

from apps.contacts.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs['placeholder'] = 'Your name'
        self.fields['email'].widget.attrs['placeholder'] = 'Your email'
        self.fields['message'].widget.attrs['placeholder'] = 'Enter your message'

