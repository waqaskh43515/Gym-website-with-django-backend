from django import forms



class userforms(forms.Form):
    GEEKS_CHOICES =( 
    ("+", "+"), 
    ("-", "-"), 
    ("*", "*"), 
    ("/", "/"),  
)
    num1=forms.CharField(label="Name",max_length=50,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    num2=forms.CharField(label="Phon",max_length=50,required=True,widget=forms.TextInput(attrs={'class':'form-control'}))
    operation=forms.ChoiceField(label="Operation", choices=GEEKS_CHOICES, required=True,widget=forms.Select(attrs={'class':'form-control'}))
