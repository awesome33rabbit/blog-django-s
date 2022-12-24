from django.db.models import QuerySet
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from django_redis import get_redis_connection
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework_extensions.cache.decorators import cache_response

from article.serializers import CustomBookSerializer
from book.models import Book, Sale
from book.serializers import BookSerializer, SaleSerializer
from django.core.cache import cache


# Create your views here.
class BookViews(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # filterset_fields = ("id", "name")

    tags = ["Book"]

    def list(self, request, *args, **kwargs):
        cache.set("key", "value")
        value = cache.get("key")
        print(value, type(value))
        
        my_cache = get_redis_connection("asd")
        my_cache.set("asd", 12345)
        return super().list(request, *args, **kwargs)


class SaleViews(ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer

    tags = ["Book - Sale"]
    http_method_names = ["get", "post"]

    # def create(self, request, *args, **kwargs):
    #     return Response()
    def list(self, request, *args, **kwargs) -> Response:
        books: QuerySet = Book.objects.all()
        serializer = CustomBookSerializer(books, many=True)
        print(serializer)
        return Response(serializer.data)
