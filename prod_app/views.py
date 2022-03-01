from django.shortcuts import render, redirect
from django.http import JsonResponse
import requests
import json
from django.db.models import Q
from prod_app.models import ElasticDemo
from django_elasticsearch_dsl_drf.viewsets import DocumentViewSet
from django_elasticsearch_dsl_drf.filter_backends import (
	FilteringFilterBackend,
	OrderingFilterBackend,
	CompoundSearchFilterBackend
	)
from prod_app.documents import *
from prod_app.serializers import *
from django.views.generic import ListView, CreateView, UpdateView
from prod_app.forms import AddProductDetails


class PublisherDocumentView(DocumentViewSet):
	document=ProductDocument
	serializer_class = ProductDocumentSerializer
	lookup_field = 'productname'
	fielddata=True
	filter_backends =[
		FilteringFilterBackend, 
		CompoundSearchFilterBackend,
		OrderingFilterBackend
		]
	search_fields=('productname',)
	multi_match_search_fields = ('productname', )
	filter_fields={
		'productname' : 'productname',
	}
	ordering_fields = {'id': None, }
	ordering = ( 'id'  ,)

def delete_product(request, elasticdemo_id):
	product_to_delete=ElasticDemo.objects.get(id=elasticdemo_id)
	product_to_delete.delete()
	return redirect('product_list.html')



def product_list(request):
    if 'q' in request.GET:
        q = request.GET['q']
        context ={'product_list': ElasticDemo.objects.filter(productname__icontains=q) }
    else:
    	context={'product_list':ElasticDemo.objects.all().order_by('-id') }
    return render(request, 'product_list.html',context)

def product_form(request,id=0):
	if request.method=='GET':
		if id==0:
			form=AddProductDetails()
		else:
			product=ElasticDemo.objects.get(pk=id)
			form= AddProductDetails(instance=product)
		return render(request, 'product_form.html',{'form':form})
	else:
		if id==0:

			form=AddProductDetails(request.POST)
		else:
			product=ElasticDemo.objects.get(pk=id)
			form=AddProductDetails(request.POST,product)
		if form.is_valid():
			form.save()
		return redirect('/product/list')

def product_delete(request,id):
	product=ElasticDemo.objects.get(pk=id)
	product.delete()
	return redirect('/product/list')