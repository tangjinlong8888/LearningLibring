from django.db import models

# Create your models here.
class Good(models.Model):
    # gname = models.CharField(max_length=20,db_column='商品名称')
    # gcount = models.IntegerField(default=0,db_column='商品数量')
    # gprice = models.DecimalField(max_digits=6,decimal_places=2,db_column='商品价格',default=0)

    class Meta:
        # db_table = 'good'
        pass