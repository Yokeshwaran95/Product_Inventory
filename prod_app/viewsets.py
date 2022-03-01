from rest_framework import viewsets
from rest_framework.decorators import api_view
from prod_app.models import ElasticDemo
from prod_app.serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
	queryset=ElasticDemo.objects.all()
	serializer_class=ProductSerializer
