import allure
from praktikum.database import Database
from data import DefaultIngredients


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
            assert (len(buns) == 3 and
                    [bun.name for bun in buns] == DefaultIngredients.BUNS_NAMES and
                    [bun.price for bun in buns] == DefaultIngredients.BUNS_PRICES)

    @allure.title('Проверка возвращаемого по умолчанию значения метода Database.available_ingredients()')
    def test_available_ingredients_return_default_buns_list(self):
        with allure.step('Создаем объект Database'):
            database = Database()
        with allure.step('Проверяем, что возвращается значение по умолчанию'):
            ingredients = database.available_ingredients()
        assert (len(ingredients) == 6 and
                set([ingredient.type for ingredient in ingredients]) == DefaultIngredients.INGREDIENTS_TYPES and
                set([ingredient.price for ingredient in ingredients]) == DefaultIngredients.INGREDIENTS_PRICES and
                [ingredient.name for ingredient in ingredients] == DefaultIngredients.INGREDIENTS_NAMES)
