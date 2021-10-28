from django import forms

class UploadFileForm(forms.Form):
    test_file = forms.FileField()


