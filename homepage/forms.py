from django import forms



class InputForm(forms.Form):
    user_input = forms.CharField(max_length=100)
    

