from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class ExpenseIncome(models.Model):
    TRANSACTION_CHOICES=[
        ('credit','Credit'),
        ('debit','Debit')
    ]
    TAX_CHOICES=[
        ('flat','Flat'),
        ('percentage','Percentage')
    ]
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    slug = models.SlugField(max_length=120, unique=True,null=True,blank=True)
    description=models.TextField(max_length=4000)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    transaction_type=models.CharField(max_length=50,choices=TRANSACTION_CHOICES)
    tax=models.DecimalField(max_digits=10,decimal_places=2,default=0)
    tax_type=models.CharField(choices=TAX_CHOICES,default='Flat')
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    

    def save(self,*args,**kwargs):

        #logic to add the slug
        if not self.slug:
            self.slug=slugify(self.title)
    



        #logic to add the tax amount
        if self.tax_type=='flat':
            self.total= self.amount+self.tax
        elif self.tax_type=='percentage':
           self.total= self.amount+((self.amount*self.tax)/100) 
        else:
            self.total= self.amount
        
        super().save(*args, **kwargs) 


