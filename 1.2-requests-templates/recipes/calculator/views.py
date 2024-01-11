from django.http import HttpResponse
from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def home(request):
    return HttpResponse('Всем привет! Укажите, пожалуйста, название рецепта.')


def recipes_view(request):
    template_name = 'calculator/index.html'

    recipe_req = str(request.path).replace("/", "")

    servings = int(request.GET.get('servings', 1))
    edited_recipe = ingredients_counting(recipe_req, servings)

    return render(request, template_name, context={'recipe': edited_recipe})


def ingredients_counting(recipe, count):
    counted_recipe = {}

    for ingredient, amount in DATA[recipe].items():
        counted_recipe[ingredient] = amount * count

    return counted_recipe
