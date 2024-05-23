from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name

class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Cart(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        items = models.ManyToManyField(Item, through='CartItem')
    
        def __str__(self):
            return f"Cart for {self.user.username}"
    
class CartItem(models.Model):
        cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
        item = models.ForeignKey(Item, on_delete=models.CASCADE)
        quantity = models.PositiveIntegerField(default=1)
    
        def __str__(self):
            return f"{self.quantity} x {self.item.name} in cart for {self.cart.user.username}"