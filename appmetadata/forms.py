from django import forms
from appmetadata.models import AppMetaData

class URLInputForm(forms.Form):

    url_name = forms.URLField(label="Enter URL",max_length=500,
                              widget= forms.TextInput(attrs={'placeholder':'Insert website Url to Fetch data', 'class':'form-control', })
                )
    
    def clean(self):
        url = self.cleaned_data.get('url_name',None)
        if not url:raise forms.ValidationError("Please provide some URL to extract Metadata")

class URLMetaData(forms.ModelForm):
    
    class Meta:
        model = AppMetaData    
        fields = ('title','meta_desc','meta_key')
    def __init__(self,*args,**kwargs):    
        super(URLMetaData,self).__init__(*args,**kwargs)
        self.fields['title'].widget.attrs.update({'class' : 'form-control'})
        self.fields['meta_desc'].widget.attrs.update({'class' : 'form-control'})
        self.fields['meta_key'].widget.attrs.update({'class' : 'form-control'})