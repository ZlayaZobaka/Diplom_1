import allure
import helpers
import pytest
from random import randint
from data import Recipes
from praktikum.burger import Burger


class TestBurger:

    @allure.title('Проверка работы метода Burger.set_buns()')
    def test_set_buns_sets_burger_buns(self):
        with allure.step('Создаем объект Burger'):
            burger = Burger()
        with allure.step(f'Добавляем в бургер булочку'):
            some_bun = helpers.get_bun()
            burger.set_buns(some_bun)

        with allure.step(f'Проверяем, что метод возвращает ожидаемое значение'):
            assert burger.bun == some_bun

    @allure.title('Проверка работы метода Burger.add_ingredient()')
    @pytest.mark.parametrize('count', ['1', '2'])
    def test_add_ingredient_ingredient_added(self, count):
        with allure.step('Создаем объект Burger'):
            burger = Burger()
        with allure.step(f'Добавляем в бургер ингредиенты'):
            some_ingredients = helpers.get_some_ingredients(count)
            for i in some_ingredients:
                burger.add_ingredient(i)

        with allure.step(f'Проверяем, что метод возвращает ожидаемое значение'):
            assert burger.ingredients == some_ingredients

    @allure.title('Проверка работы метода Burger.remove_ingredient()')
    @pytest.mark.parametrize('count', ['1', '5'])
    def test_remove_ingredient_ingredient_removed(self, count):
        with allure.step('Создаем объект Burger'):
            burger = Burger()
        with allure.step(f'Добавляем в бургер ингредиенты'):
            some_ingredients = helpers.get_some_ingredients(count)
            for i in some_ingredients:
                burger.add_ingredient(i)

        random_index = randint(0, len(some_ingredients) - 1)
        with allure.step(f'Удаляем из бургера ингредиент № {random_index}'):
            burger.remove_ingredient(random_index)

        with allure.step(f'Проверяем, что метод возвращает ожидаемое значение'):
            del some_ingredients[random_index]
            assert burger.ingredients == some_ingredients

    @allure.title('Проверка работы метода Burger.move_ingredient()')
    @pytest.mark.parametrize('count', ['1', '5'])
    def test_move_ingredient_ingredient_moved(self, count):
        with allure.step('Создаем объект Burger'):
            burger = Burger()
        with allure.step(f'Добавляем в бургер ингредиенты'):
            some_ingredients = helpers.get_some_ingredients(count)
            for i in some_ingredients:
                burger.add_ingredient(i)

        random_index1 = randint(0, len(some_ingredients) - 1)
        random_index2 = randint(0, len(some_ingredients) - 1)
        with allure.step(f'Меняем  ингредиенты № {random_index1} и № {random_index2} местами'):
            burger.move_ingredient(random_index1, random_index2)

        with allure.step(f'Проверяем, что метод возвращает ожидаемое значение'):
            some_ingredients.insert(random_index2, some_ingredients.pop(random_index1))
            assert burger.ingredients == some_ingredients

    @allure.title('Проверка работы метода Burger.get_price()')
    @pytest.mark.parametrize('count', ['1', '5'])
    def test_get_price_price_calculated(self, count):
        with allure.step('Создаем объект Burger'):
            burger = Burger()
        with allure.step(f'Добавляем в бургер булочку'):
            some_bun = helpers.get_bun()
            burger.set_buns(some_bun)
        with allure.step(f'Добавляем в бургер ингредиенты'):
            some_ingredients = helpers.get_some_ingredients(count)
            for i in some_ingredients:
                burger.add_ingredient(i)

        with allure.step(f'Проверяем, что метод возвращает ожидаемую цену'):
            buns_price = some_bun.price * 2
            ingredients_price = sum(list(map(lambda x: x.price, some_ingredients)))
            assert burger.get_price() == buns_price + ingredients_price

    @allure.title('Проверка работы метода Burger.get_receipt()')
    @pytest.mark.parametrize('recipe', [Recipes.RECIPE_1, Recipes.RECIPE_2])
    def test_get_receipt_return_expected_receipt(self, recipe):
        with allure.step('Создаем объект Burger'):
            burger = Burger()
        with allure.step(f'Добавляем в бургер булочку'):
            bun = helpers.get_recipe_bun(recipe)
            burger.set_buns(bun)
        with allure.step(f'Добавляем в бургер ингредиенты'):
            some_ingredients = helpers.get_recipe_ingredient(recipe)
            for i in some_ingredients:
                burger.add_ingredient(i)

        with allure.step(f'Проверяем, что в рецепт совпадает с ожидаемым'):
            assert burger.get_receipt() == recipe['text']
