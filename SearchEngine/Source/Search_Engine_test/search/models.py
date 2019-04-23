from django.db import models

# Create your models here.
class SearchModel(models.Model):
    search_content=models.CharField(max_length=120,null=False,blank=False)