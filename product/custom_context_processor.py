from .models import Category


def category_render(request):
    return {
        'categories': Category.objects.all()
    }
