from django.contrib import admin
from django.urls import path, include
from prod_app.views import (  PublisherDocumentView,
	product_list,product_form, product_delete)
from prod_app.viewsets import ProductViewSet







urlpatterns = [
	path('',product_form,name="product_insert"),
	path('<int:id>/',product_form,name="product_update"),
	path('list/',product_list,name='home'),
	path('search/',PublisherDocumentView.as_view({'get':'list'})),
	path('delete/<int:id>/',product_delete,name="product_delete")
]