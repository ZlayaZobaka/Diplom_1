from faker import Faker
from unittest.mock import Mock


class DefaultIngredients:
    BUNS_NAMES = ['black bun', 'white bun', 'red bun']
    BUNS_PRICES = [100, 200, 300]
    INGREDIENTS_TYPES = {'SAUCE', 'FILLING'}
    INGREDIENTS_NAMES = ['hot sauce', 'sour cream', 'chili sauce', 'cutlet', 'dinosaur', 'sausage']
    INGREDIENTS_PRICES = {100, 200, 300}


class TestData:
    """
    Класс с тестовыми данными.
    """
    @staticmethod
    def get_bun():
        mock_bun = Mock()
        mock_bun.name = Faker().word()
        mock_bun.price = Faker().random_int()
        mock_bun.get_price.return_value = mock_bun.price
        mock_bun.get_name.return_value = mock_bun.name

        return mock_bun

    @staticmethod
    def get_ingredient():
        mock_ingredient = Mock()
        mock_ingredient.type = Faker().word()
        mock_ingredient.name = Faker().word()
        mock_ingredient.price = Faker().random_int()
        mock_ingredient.get_price.return_value = mock_ingredient.price
        mock_ingredient.get_name.return_value = mock_ingredient.name
        mock_ingredient.get_type.return_value = mock_ingredient.type

        return mock_ingredient




