from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home_page, about_us_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('about_us', about_us_page),
    path('products/', include('product.urls')),
    path('account/', include('userprofile.urls')),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
