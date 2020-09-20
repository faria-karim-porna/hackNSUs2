from django.db import models

class Purchase(models.Model):
    psupplier = models.CharField(max_length=30)
    psupplier_contact = models.CharField(max_length=20)
    pproduct_category =  models.CharField(max_length=30)
    pproduct_brand =  models.CharField(max_length=30)
    pproduct_name =  models.CharField(max_length=30)
    pproduct =  models.CharField(max_length=30)
    pquantity = models.IntegerField()
    peach_price =  models.DecimalField(max_digits=5, decimal_places=2)
    ptotal_price =  models.DecimalField(max_digits=8, decimal_places=2)
    ppurchase_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    class Meta:
        db_table = "purchase"

