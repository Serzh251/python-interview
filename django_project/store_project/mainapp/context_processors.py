from mainapp.models import Category


def category(request):
    return {"category_menu": Category.objects.all()}