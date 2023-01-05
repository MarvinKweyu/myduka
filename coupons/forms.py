from django import forms
from coupons.models import Coupon


class CouponApplyForm(forms.Form):
    """Manage the entry of coupon code from the client"""

    code = forms.CharField()
