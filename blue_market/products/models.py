from django.db import models
from django.conf import settings

# MODELO DE PRODUCTO
class Product(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="media", null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
    	return self.title

    @property
    def comments(self):
    	return self.comment_set.all()

    class Meta:
        ordering = ['-created_at']

# MODELO DE COMENTARIO
class Comment(models.Model):
 	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
 	post = models.ForeignKey(Product, on_delete=models.CASCADE)
 	text = models.TextField()
 	created_at = models.DateTimeField(auto_now_add=True)
 	
 	def __str__(self):
 		return self.text

 	class Meta:
 		ordering = ['-created_at']

# MODELO DE RESPUESTA DE COMENTARIO
class Reply(models.Model):
 	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="replies")
 	parent_comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="replies")
 	text = models.CharField(max_length=100)
 	created_at = models.DateTimeField(auto_now_add=True)

 	def __str__(self):
 		return self.text

# MODELO DE REVIEW
class ReviewRating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="ratings")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
    rating = models.FloatField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


# MODELO DE TRANSACCION
class Transaction(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('debit', 'Debito'),
        ('currency', 'Divisas')
    ]
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="purchase")
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="seller")
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    payment_method = models.CharField(max_length=10, choices=PAYMENT_METHOD_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['-created_at']