import allure
import helpers
from praktikum.database import Database
from data import Recipes


class TestDatabase:
    @allure.title('Проверка работы метода Database.available_buns()')
    def test_available_buns_return_expected_buns_list(self):
        with allure.step('Создаем объект Database'):
            database = Database()
        with allure.step('Переопределяем значение аттрибута buns'):
            database.buns = ['test1', 'test2']

        with allure.step('Проверяем, что возвращается переопределенное значение'):
            assert database.available_buns() == ['test1', 'test2']

    @allure.title('Проверка работы метода Database.available_ingredients()')
    def test_available_ingredients_return_expected_ingredients_list(self):
        with allure.step('Создаем объект Database'):
            database = Database()
        with allure.step('Переопределяем значение аттрибута ingredients'):
            database.ingredients = ['test1', 'test2']

        with allure.step('Проверяем, что возвращается переопределенное значение'):
            assert database.available_ingredients() == ['test1', 'test2']

    @allure.title('Проверка возвращаемого по умолчанию значения метода Database.available_buns()')
    def test_available_buns_return_default_buns_list(self):
        with allure.step('Создаем объект Database'):
            database = Database()
        with allure.step('Проверяем, что возвращается значение по умолчанию'):
            buns = database.available_buns()
            expected_buns = helpers.get_recipe_buns(Recipes.DEFAULT_DB)
            assert helpers.compare(buns, expected_buns)

    @allure.title('Проверка возвращаемого по умолчанию значения метода Database.available_ingredients()')
    def test_available_ingredients_return_default_buns_list(self):
        with allure.step('Создаем объект Database'):
            database = Database()
        with allure.step('Проверяем, что возвращается значение по умолчанию'):
            ingredients = database.available_ingredients()
            expected_ingredients = helpers.get_recipe_ingredients(Recipes.DEFAULT_DB)
        assert helpers.compare(ingredients, expected_ingredients)
