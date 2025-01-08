# urls.py
from django.urls import path
from .views import (
    UserCreateView, UserListView,
    ProductListCreateView, ProductDetailView, ProductSearchView
)
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # JWT authentication endpoints
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    # User endpoints
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/register/', UserCreateView.as_view(), name='user-register'),

    # Product endpoints
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/search/', ProductSearchView.as_view(), name='product-search'),
]

