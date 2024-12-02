from django.urls import include, path
from .views import (
	add_product, 
	list_product, 
	modify_product, 
	delete_product, 
	product_detail,
	comment_sent,
	reply_sent,
	confirm_product,
	confirm_product_user_data,
	purchases_list,
	sales_list,
	review_rating,
	import_products,
	ReportProductExcel
)

urlpatterns = [
	path('create/', add_product, name="create_view"),
	path('import-products', import_products, name="import_products"),
	path('list-products/', list_product, name="list_products"),
	path('resport-product/', ReportProductExcel.as_view(), name='report_product'),
	path('modify-product/<id>', modify_product, name="upladoad_products"),
	path('delete-product/<id>', delete_product, name="delete_product"),
	path('detail_product/<pk>', product_detail, name="detail_product"),
	path('comment/<pk>', comment_sent, name="comment_sent"),
	path('reply_comment/<pk>', reply_sent, name="reply_sent"),
	path('confirm_product/<pk>', confirm_product, name="confirm_product"),
	path('confirm_product_data/<pk>', confirm_product_user_data, name="confirm_product_user_data"),
	path('my_purchases/', purchases_list, name='purchases'),
	path('my_sales/', sales_list, name='sales'),
	path('review_rating/<pk>', review_rating, name='review'),
]

