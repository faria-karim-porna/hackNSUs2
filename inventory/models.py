from django.db import models
# purchase table
class Purchase(models.Model):
    psupplier = models.CharField(max_length=30)
    psupplier_contact = models.CharField(max_length=20)
    pproduct_category =  models.CharField(max_length=30)
    pproduct_brand =  models.CharField(max_length=30)
    pproduct_name =  models.CharField(max_length=30)
    pquantity = models.IntegerField()
    peach_price =  models.FloatField()
    ptotal_price =  models.FloatField()
    ppurchase_date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    class Meta:
        db_table = "purchase"

# stored product table
class Stored_Product(models.Model):
    spproduct_category =  models.CharField(max_length=30)
    spproduct_brand =  models.CharField(max_length=30)
    spproduct_name =  models.CharField(max_length=30)
    spquantity = models.IntegerField()
    speach_price =  models.FloatField()
    class Meta:
        db_table = "stored_product"

# stock out table
class Stock_Out(models.Model):
    soproduct_category =  models.CharField(max_length=30)
    soproduct_brand =  models.CharField(max_length=30)
    soproduct_name =  models.CharField(max_length=30)
    soquantity = models.IntegerField()
    soeach_price =  models.FloatField()
    class Meta:
        db_table = "stock_out"

# sale table
class Sale(models.Model):
    sbuyer = models.CharField(max_length=30)
    sbuyer_contact = models.CharField(max_length=20)
    sproduct_category =  models.CharField(max_length=30)
    sproduct_brand =  models.CharField(max_length=30)
    sproduct_name =  models.CharField(max_length=30)
    squantity = models.IntegerField()
    seach_price =  models.FloatField()
    stotal_price =  models.FloatField()
    ssale_date = models.DateField(auto_now=False, auto_now_add=True, blank=True)
    class Meta:
        db_table = "sale"

