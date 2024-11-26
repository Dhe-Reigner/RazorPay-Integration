from django.db import models

# Create your models here.
# class Coffee(models.Model):
#     name = models.CharField(max_length=100)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     quantity = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     is_active = models.BooleanField(default=True)
#     customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
#     order = models.ForeignKey('Order', on_delete=models.CASCADE, null=True)
#     payment = models.ForeignKey('Payment', on_delete=models.CASCADE, null=True)
    
#     class Meta:
#         verbose_name = 'Coffee'
#         verbose_name_plural = 'Coffees'
#         ordering = ['-created_at']
        
        
class Coffee(models.Model):
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name