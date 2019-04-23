from django.forms import  ModelForm
from search.models import SearchModel

class SearchForm(ModelForm):
    class Meta:
        model=SearchModel
        fields=['search_content']



