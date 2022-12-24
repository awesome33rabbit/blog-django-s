from django.shortcuts import render
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import ArticleCategory, ArticleTag, Article
from .serializers import ArticleCategorySerializer, ArticleTagSerializer, ArticleSerializer, ArticleDetailSerializer


# Create your views here.
class CategoryViews(ModelViewSet):
    queryset = ArticleCategory.objects.all()
    serializer_class = ArticleCategorySerializer
    permission_classes = [AllowAny]
    tags = ["Article - Category"]


class TagViews(ModelViewSet):
    queryset = ArticleTag.objects.all()
    serializer_class = ArticleTagSerializer

    tags = ["Article - Tag"]


class ArticleViews(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # permission_classes = [IsAdminUser]

    tags = ["Article"]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())  # 100

        queryset = self.paginate_queryset(queryset)  # page = queryset[:24]
        # serializer = self.get_serializer(page, many=True)
        serializer = ArticleDetailSerializer(queryset, many=True)
        return self.get_paginated_response(serializer.data)
