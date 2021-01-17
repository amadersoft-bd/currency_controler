from .models import Notification
from django import forms


class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification

        fields=('title','body','status','duration')