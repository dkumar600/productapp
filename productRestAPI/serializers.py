from rest_framework import serializers
from productRestAPI.models import ProductList

class ProductListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductList
        fields = "__all__"