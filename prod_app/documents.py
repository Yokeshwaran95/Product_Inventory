from django_elasticsearch_dsl import (
	Document, fields, Index
)
from prod_app.models import ElasticDemo


PUBLISHER_INDEX=Index('elastic_demo')

PUBLISHER_INDEX.settings(
	number_of_shards = 1,
	number_of_replicas =1
	)

@PUBLISHER_INDEX.doc_type
class ProductDocument(Document):
	id= fields.IntegerField(attr="id")
	productname=fields.TextField(
		fields={
			"raw":{
				"type": "keyword",
			}
		}
		)
	productprice= fields.IntegerField(attr="productprice")
	quantity= fields.IntegerField(attr="quantity")

	class Django(object):
		model=ElasticDemo
