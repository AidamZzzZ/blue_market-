from django.contrib import admin
from .models import (
	Product, 
	Comment, 
	Reply,
	ReviewRating,
	Transaction
)

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
	list_display = ['user', 'title', 'description', 'price']

@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
	list_display = ['id', 'author', 'post', 'created_at']

@admin.register(Reply)
class ReplyModelAdmin(admin.ModelAdmin):
	list_display = ['id', 'author', 'parent_comment', 'created_at']


@admin.register(ReviewRating)
class ReviewRatingModelAdmin(admin.ModelAdmin):
	list_display = ['id', 'product', 'user', 'rating']

@admin.register(Transaction)
class TransactionModelAdmin(admin.ModelAdmin):
	list_display = ['id', 'buyer', 'seller', 'product', 'quantity', 'payment_method']