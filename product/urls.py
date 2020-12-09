from django.urls import path
from .views import ProductList, ProductDetail

urlpatterns = [
    path('', ProductList.as_view()),
    path('<pk>/<product_name>', ProductDetail.as_view())
]
