import allure
import pytest
from praktikum.bun import Bun


class TestBun:
    @allure.title('Проверка работы метода Bun.get_name()')
    @pytest.mark.parametrize(
        'name, price',
        [
            ['Бородинский',  50],
            ['tortilla', 100]
        ]
    )
    def test_get_name_return_expected_name(self, name, price):
        with allure.step(f'Создаем булочку с параметрами '
                         f'name: {name}, price: {price}'):
            bun = Bun(name, price)

        with allure.step(f'Проверяем, что возвращается ожидаемое имя: {name}'):
            assert bun.get_name() == name

    @allure.title('Проверка работы метода Bun.get_price()')
    @pytest.mark.parametrize(
        'name, price',
        [
            ['Бородинский', 50],
            ['tortilla', 100]
        ]
    )
    def test_get_price_return_expected_price(self, name, price):
        with allure.step(f'Создаем булочку с параметрами '
                         f'name: {name}, price: {price}'):
            bun = Bun(name, price)

        with allure.step(f'Проверяем, что возвращается ожидаемая цена: {price}'):
            assert bun.get_price() == price
