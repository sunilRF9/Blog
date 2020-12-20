from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Post


@registry.register_document
class PostDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'posts'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Post 
        fields = [
            'title',
            'content',
            'category',
        ]
        # auto_refresh = False
        # queryset_pagination = 5000
