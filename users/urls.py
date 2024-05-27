from django.urls import path

from users.views import CategoryViewSet, ProductListView, ProductDetailView

urlpatterns = [
    path('category/', CategoryViewSet.as_view()),
    path('products/', ProductListView.as_view()),
    path('products/<int:pk>/', ProductDetailView.as_view()),
]
