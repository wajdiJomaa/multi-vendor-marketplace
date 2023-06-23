from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import *

urlpatterns = [
    path("", getRoutes),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register_customer/', RegisterCustomerView.as_view()),
    path('register_vendor/', RegisterVendorView.as_view()),
    path('add_product/', AddProductView.as_view()),
    path('get_categories/', GetCategoryView.as_view())
    # path('add_product_options/', AddProductOptionsView.as_view())
]