from django.shortcuts import render, get_object_or_404

from utils.decorators import key_required

from .models import Film, Category

@key_required
def index(request, template_name):
    films = Film.objects.filter(active=True)
    return render(request, template_name, {
        'films': films,
    })

@key_required
def show_category(request, category_slug, template_name):
    category = get_object_or_404(Category, slug=category_slug)
    films = category.film_set.filter(active=True)
    return render(request, template_name, {
        'category': category,
        'films': films,
    })