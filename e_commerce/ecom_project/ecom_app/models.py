from django.db import models
from django.urls import reverse


# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    desc=models.TextField(null=True)
    image=models.ImageField(upload_to='Category',blank=True)
    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'
    def get_url(self):
        return reverse('ecom_app:all_product_cat',args=[self.slug])
    def __str__(self):
        return '{}'.format(self.name)
class product(models.Model):
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    desc=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    categ=models.ForeignKey(category,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='Products',blank=True)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateField(auto_now_add=True)
    update=models.DateField(auto_now=True)
    class Meta:
        ordering=('name',)
        verbose_name='product'
        verbose_name_plural='products'
    def get_url(self):
        return reverse('ecom_app:prodetails',args=[self.categ.slug,self.slug])
    def __str__(self):
        return '{}'  .format(self.name)