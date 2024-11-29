from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet

from blog.models import Category, Article
from blog.serializers import CategorySerializer, ArticleSerializer, UserSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class ArticleViewSet(ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()