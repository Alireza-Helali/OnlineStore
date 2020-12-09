from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Gallery, Product, Category, Tag, SubCategory


# Register your models here.
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']


admin.site.register(Product)
admin.site.register(Gallery)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(SubCategory, SubCategoryAdmin)
