from django import forms


class BioForm(forms.Form):
    input_seq = forms.CharField(label='Input sequence', widget=forms.Textarea)
