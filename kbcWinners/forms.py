from django.forms import ModelForm
from .models import Contact,Winner


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class WinnerForm(ModelForm):
    class Meta:
        model=Winner
        exclude=['winner_name','pub_date','amount']