from django import forms
from .models import (
	Product, 
	Comment, 
	Reply,
	ReviewRating,
	Transaction,
)

# FORMULARIO DE PRODUCTO
class ProductsForm(forms.ModelForm):

	class Meta:
		model = Product
		fields = ('title', 'description', 'price', 'image', 'stock')

# FORMULARIO DE COMENTARIOS
class CommentsForm(forms.ModelForm):

	class Meta:
		model = Comment
		fields = ('text',)

# FORMULARIO DE RESPUESTAS A COMENTARIOS
class ReplyForm(forms.ModelForm):

	class Meta:
		model = Reply
		fields = ['text',]

# FORMULARIO DE REVIEWS
class ReviewRatingForm(forms.ModelForm):

	class Meta:
		model = ReviewRating
		fields = ['rating', 'comment']

# FORMULARIO DE TRANSACCION DE COMPRAS
class TransactionForm(forms.ModelForm):

	class Meta:
		model = Transaction
		fields = ['quantity', 'payment_method']

class ExcelUploadForm(forms.Form):
	file = forms.FileField(label='Upload Excel')