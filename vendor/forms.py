from django import forms
from django.utils.translation import gettext_lazy as _

from .models import Vendor


class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'
        labels = {
            'vendor_name': _('攤販名稱'),
            'store_name': _('店名'),
            'phone_number': _('電話'),
            'address': _('地址'),
        }
