from django.db import models

# Create your models here.
class Product(models.Model) :
    product_id = models.BigAutoField(primary_key = True)
    product_name = models.CharField(max_length = 50)
    categery = models.CharField(max_length = 50, default = "")
    sub_category = models.CharField(max_length = 100, default = "")
    product_description = models.CharField(max_length = 300)
    pub_date = models.DateField('')
    price = models.IntegerField(default = 0)
    images = models.ImageField(upload_to = "blog/images", default = "")

    def __str__(self):
        return self.product_name