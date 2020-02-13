from django import forms
from .models import writing

#models.py에 있는 데이터 바탕으로 form 생성... ModelForm
#아니라면 그냥 그자리에 Form
class writing_post(forms.ModelForm):
    class Meta:
        model = writing
        fields = ['title','text']

# class writing_post(forms.Form):
#     email = forms.EmailField()
#     files = forms.FileField()
#     url = forms.URLField()
#     words = forms.CharField(max_length = 200)
#     max_number = forms.ChoiceField(choices=[('1','one'),('2','two'),('3','three')])