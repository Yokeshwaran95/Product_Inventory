# Product_Inventory
TechStack: Django, API, Riot.Js, ElasticSearch

Objective:
  To perform Create, Update, Search List and Delete product details from inventory app with both UI and API
 
 Prerequisites:
  Python 3.x
  pip install requirements.txt
  Make sure elastic search is running. Name: elastic_demo
 
 API calls:
 
 Django part:

GET: Read all        http://127.0.0.1:8000/api/product/
     Read with Id    http://127.0.0.1:8000/api/product/<id>   	
POST: Add            http://127.0.0.1:8000/api/product/
PUT:  Update	     http://127.0.0.1:8000/api/product/<id>
DELETE: Delete	     http://127.0.0.1:8000/api/product/<id>


Search api:          http://127.0.0.1:8000/product/search/?search=<search_string>


Elastic Search Part:

Search api:          http://127.0.0.1:9200/elastic_demo/_search?q=<search_string>
