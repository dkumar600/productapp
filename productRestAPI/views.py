from django.shortcuts import render
from rest_framework import viewsets
from productRestAPI.models import ProductList
from productRestAPI.serializers import ProductListSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = ProductList.objects.all()
    serializer_class = ProductListSerializer
# Create your views here.
