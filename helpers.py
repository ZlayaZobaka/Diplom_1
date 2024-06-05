import allure
from faker import Faker
from unittest.mock import Mock


@allure.title('Создаем Mock-булочку')
def get_bun(bun=None):
    mock_bun = Mock()
    mock_bun.name = bun[0] if bun else Faker().word()
    mock_bun.price = bun[1] if bun else Faker().random_int()
    mock_bun.get_price.return_value = mock_bun.price
    mock_bun.get_name.return_value = mock_bun.name

    return mock_bun


@allure.title('Создаем Mock-ингредиент')
def get_ingredient(ingredient=None):
    mock_ingredient = Mock()
    mock_ingredient.type = ingredient[0] if ingredient else Faker().word()
    mock_ingredient.name = ingredient[1] if ingredient else Faker().word()
    mock_ingredient.price = ingredient[2] if ingredient else Faker().random_int()
    mock_ingredient.get_price.return_value = mock_ingredient.price
    mock_ingredient.get_name.return_value = mock_ingredient.name
    mock_ingredient.get_type.return_value = mock_ingredient.type

    return mock_ingredient


@allure.title('Создаем случайный список ингредиентов')
def get_some_ingredients(count):
    return [get_ingredient() for _ in range(int(count))]


@allure.title('Извлекаем из рецепта булочку')
def get_recipe_bun(recipe):
    return get_bun(recipe['bun'])


@allure.title('Извлекаем из рецепта ингредиенты')
def get_recipe_ingredient(recipe):
    return [get_ingredient(x) for x in recipe['ingredients']]
