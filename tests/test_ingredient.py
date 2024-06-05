import allure
import pytest
from praktikum.ingredient import Ingredient


class TestIngredient:
    @allure.title('Проверка работы метода Ingredient.get_price()')
    @pytest.mark.parametrize(
        'ingredient_type, name, price',
        [
            ['соус', 'майонез',  42],
            ['topping', 'cream', 17]
        ]
    )
    def test_get_price_return_expected_price(self, ingredient_type, name, price):
        with allure.step(f'Создаем булочку с параметрами '
                         f'ingredient_type: {ingredient_type} name: {name}, price: {price}'):
            ingredient = Ingredient(ingredient_type, name, price)

        with allure.step(f'Проверяем, что возвращается ожидаемая цена: {price}'):
            assert ingredient.get_price() == price

    @allure.title('Проверка работы метода Ingredient.get_name()')
    @pytest.mark.parametrize(
        'ingredient_type, name, price',
        [
            ['соус', 'майонез', 42],
            ['topping', 'cream', 17]
        ]
    )
    def test_get_name_return_expected_name(self, ingredient_type, name, price):
        with allure.step(f'Создаем булочку с параметрами '
                         f'ingredient_type: {ingredient_type} name: {name}, price: {price}'):
            ingredient = Ingredient(ingredient_type, name, price)

        with allure.step(f'Проверяем, что возвращается ожидаемое имя: {name}'):
            assert ingredient.get_name() == name

    @allure.title('Проверка работы метода Ingredient.get_type()')
    @pytest.mark.parametrize(
        'ingredient_type, name, price',
        [
            ['соус', 'майонез', 42],
            ['topping', 'cream', 17]
        ]
    )
    def test_get_type_return_expected_type(self, ingredient_type, name, price):
        with allure.step(f'Создаем булочку с параметрами '
                         f'ingredient_type: {ingredient_type} name: {name}, price: {price}'):
            ingredient = Ingredient(ingredient_type, name, price)

        with allure.step(f'Проверяем, что возвращается ожидаемый тип: {ingredient_type}'):
            assert ingredient.get_type() == ingredient_type
