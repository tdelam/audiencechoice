from films.models import Category


def category_list(request):
    return {
        'categories': Category.objects.all(),
        'request': request
    }
