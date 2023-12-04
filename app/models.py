from django.db import models

# Create your models here.
class productcatagory(models.Model):
    categoryname=models.CharField(max_length=100)
    categoryid=models.IntegerField()
    def __str__(self):
        return self.categoryname
    
class product(models.Model):
    categoryname=models.ForeignKey(productcatagory,on_delete=models.CASCADE)
    pname=models.CharField(max_length=100)
    pid=models.PositiveIntegerField(primary_key=True)
    price=models.DecimalField(max_digits=9,decimal_places=2)
    date=models.DateField()
    def __str__(self):
        return self.pname     