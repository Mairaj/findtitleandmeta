from django import forms
from models import WebsiteData

class UrlInputForm(forms.Form):
	urlname = forms.URLField(max_length=500, 
								widget= forms.TextInput(attrs={'placeholder':'Insert website Url to Fetch data'})
								)


class datainputform(forms.ModelForm):
	class Meta:
		model = WebsiteData

