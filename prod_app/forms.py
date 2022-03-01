from django.forms import ModelForm
from prod_app.models import ElasticDemo


class AddProductDetails(ModelForm):
	class Meta:
		model=ElasticDemo
		fields='__all__'
		labels={
			'productname': "Product Name",
			'productprice': "Price"

		}


