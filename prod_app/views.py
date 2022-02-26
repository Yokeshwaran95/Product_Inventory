from django.shortcuts import render
from django.http import JsonResponse
import requests
import json
from prod_app.models import ElasticDemo

# Create your views here.

def generate_random_data():
	url='https://newsapi.org/v2/everything?q=apple&from=2021-04-23&to=2021-04-23&sortBy=popularity&apiKey=827705eea42e455cba8bf4afafc7da90'
	r=requests.get(url)
	payload=json.loads(r.text)
	count=1
	#print(payload.get('articles'))
	for data in range(100):
		print(count)
		ElasticDemo.objects.create(
			productname= 'productname_'+str(count),
			productprice=count*10,
			quantity=count
			)
		count+=1

def index(request):
	generate_random_data()
	return JsonResponse({'status':200})