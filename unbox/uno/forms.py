from uno.models import Question_m
from django import forms

Location = (
    ('goa','Goa'),
    ('mumbai','Mumbai'),
    ('bangalore','Bangalore'),
)

class Question_f(forms.ModelForm):
    location = forms.ChoiceField(choices=Location,
                 help_text="Location of the Scrap generating Company")
    name = forms.CharField(max_length=100,required=True,help_text="Name")
    contact_info = forms.CharField(max_length=100,required=True,help_text="Contact Information")
    item = forms.CharField(max_length=100,required=True,help_text="Item")
    quantity = forms.CharField(max_length=100,required=True,help_text="Quantity")
    price = forms.CharField(max_length=100,required=True,help_text="Price quoted")
    additional_info = forms.CharField(max_length=1000,help_text="Additional Information")
    certificates = forms.URLField(max_length=200, help_text="Google drive link to your authorized license", required=False)

    class Meta:
        model = Question_m
        fields = ['name', 'contact_info', 'item', 'quantity', 'price', 'additional_info','location', 'certificates']
