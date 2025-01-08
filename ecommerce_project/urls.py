# urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # Admin interface (optional)
    path('admin/', admin.site.urls),

    # API URLs
    path('api/products/', include('product_api.urls')),  # Routes to the product_api app

    # JWT authentication URLs
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Obtain JWT token
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),  # Refresh JWT token
]

