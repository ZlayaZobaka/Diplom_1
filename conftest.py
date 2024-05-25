import allure
import pytest
from data import TestData
from praktikum.burger import Burger
from praktikum.database import Database


@allure.title('Создаем объект Database')
@pytest.fixture(scope='function')
def database():
    return Database()


@allure.title('Создаем объект Burger')
@pytest.fixture(scope='function')
def burger():
    return Burger()


@allure.title('Создаем случайную булочку')
@pytest.fixture(scope='function')
def some_bun():
    return TestData.get_bun()


@allure.title('Создаем случайный список ингредиентов')
@pytest.fixture(scope='function')
def some_ingredients(request):
    return [TestData.get_ingredient() for _ in range(int(request.param))]
