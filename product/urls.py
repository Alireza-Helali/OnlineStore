from django.urls import path
from .views import ProductList, ProductDetail, ShowByCategory

urlpatterns = [
    path('', ProductList.as_view()),
    path('<pk>/<product_name>', ProductDetail.as_view()),
    path('<cat_name>', ShowByCategory.as_view())

]
