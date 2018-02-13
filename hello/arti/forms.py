from django import forms
#for creating our own forms
from.import models
#from the current directory denoted by the dot
class CreateArticle(forms.ModelForm):
    class Meta:#which feild to be inherit m in meta should be in capital
       model=models.Articles
       fields=['title','body','slug','thumb']
