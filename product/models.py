from django.db import models
class Product(models.Model):
    title = models.CharField(max_length=250)
    price = models.IntegerField()
    description = models.TextField(max_length=500)
    created_data = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.title

class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField(null=True)







