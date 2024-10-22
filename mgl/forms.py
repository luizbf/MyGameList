from django import forms

class RegisterForm(forms.Form):
          
    game_image = forms.ImageField(required=False)
    game_name = forms.CharField()
    hours_taken = forms.CharField(required=False, empty_value='???')   
    date_finished = forms.CharField(required=False, max_length=10, empty_value="???")   
    about = forms.CharField(widget=forms.Textarea, required=False)
    other = forms.CharField(widget=forms.Textarea, required=False)
