import allure
from faker import Faker
from unittest.mock import Mock


@allure.title('Создаем случайную булочку')
def get_bun():
    mock_bun = Mock()
    mock_bun.name = Faker().word()
    mock_bun.price = Faker().random_int()
    mock_bun.get_price.return_value = mock_bun.price
    mock_bun.get_name.return_value = mock_bun.name

    return mock_bun


@allure.title('Создаем случайный ингредиент')
def get_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.type = Faker().word()
    mock_ingredient.name = Faker().word()
    mock_ingredient.price = Faker().random_int()
    mock_ingredient.get_price.return_value = mock_ingredient.price
    mock_ingredient.get_name.return_value = mock_ingredient.name
    mock_ingredient.get_type.return_value = mock_ingredient.type

    return mock_ingredient


@allure.title('Создаем случайный список ингредиентов')
def get_some_ingredients(count):
    return [get_ingredient() for _ in range(int(count))]
