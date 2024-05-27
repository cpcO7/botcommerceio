from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView, UpdateAPIView

from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CategoryViewSet(ListAPIView, CreateAPIView, DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductListView(ListAPIView, CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
