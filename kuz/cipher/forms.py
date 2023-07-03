from django import forms
from django.db.models import fields
from .models import *


class UploadImg(forms.ModelForm):
    class Meta:
        model = Image_file
        fields = ('title', 'key','original_img', 'alg_var')


        