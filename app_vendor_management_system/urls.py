
from django.urls import path
from .views import VendorView, PurchaseOrderView, VendorPerformanceView
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)

urlpatterns = [
    path('vendors/', VendorView.as_view(), name="Vendor List"),
    path('vendors/<int:id>/', VendorView.as_view(), name="Vendor View"),
    path('purchase_orders/', PurchaseOrderView.as_view(), name="Purchase Order List"),
    path("purchase_orders/<int:id>/", PurchaseOrderView.as_view(), name="Purchase Order View"),
    path('vendors/<int:id>/performance/', VendorPerformanceView.as_view(), name="Vendor Performance"),
    path('both_tokens/',TokenObtainPairView.as_view(),name='Both Tokens'),
    path("new_token/",TokenRefreshView.as_view(),name='New Token'),
]
