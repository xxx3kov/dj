from multiprocessing import context

from django.shortcuts import render
from django.http import HttpResponse

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
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def start_page(request):
    dishes = ', '.join(DATA.keys())
    return HttpResponse(f'Привет, доступные рецепты: {dishes}')


def recipe_view(request, dish):
    context = {
        'recipe': {}
        }
    count_dishes = int(request.GET.get('servings', 1))
    ingredients = DATA[dish]
    for key, value in ingredients.items():
        context['recipe'][key] = value * count_dishes
    
    return render(request, 'calculator/index.html', context)