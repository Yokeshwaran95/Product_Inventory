from prod_app.models import ElasticDemo
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from prod_app.documents import *
from rest_framework import serializers


class ProductDocumentSerializer(DocumentSerializer):
	class Meta:
		model = ElasticDemo
		document = ProductDocument

		fields = ('productname','productprice','quantity')

		def get_location(self,obj):
			try:
				return obj.location.to_dict()
			except:
				return {}

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model=ElasticDemo
		fields="__all__"